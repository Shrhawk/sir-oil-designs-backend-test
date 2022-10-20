from fastapi import Depends, FastAPI, HTTPException, status

from auth.jwt_bearer import JWTBearer
from database.db import initiate_database
from database.initial_data import initiate_db
from routes.user import router as user_router

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


@app.get("/initiate_data", tags=["Root"])
async def initiate_data():
    try:
        await initiate_db()
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {"message": "Initial data created"}


app.include_router(user_router, tags=["User"], prefix="/user")
