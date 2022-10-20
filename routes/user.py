from beanie import PydanticObjectId
from fastapi import APIRouter, Body, HTTPException, Depends, status
from passlib.context import CryptContext

from auth.jwt_bearer import get_current_user
from auth.jwt_handler import sign_jwt
from crud.user import get_user_detail
from models.users_model import User
from schemas.users_schema import UserData, UserSignIn, UserSignUp, UserDetails

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


@router.post("/login")
async def user_login(user_credentials: UserSignIn = Body(...)) -> dict:
    """
    User login route.
    """
    user_exists = await User.find_one(User.username == user_credentials.username)
    if user_exists:
        password = hash_helper.verify(user_credentials.password, user_exists.password)
        if password:
            return await sign_jwt(str(user_exists.id))
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect username or password")
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect username or password")


@router.post("/user_signup", response_model=UserSignUp)
async def user_signup(user: UserData = Body(...)) -> User:
    """
    User signup route.
    """
    user_username = await User.find_one(User.username == user.username or User.email == user.email)
    if user_username:
        if user_username.username == user.username:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")
        if user_username.email == user.email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
    user.password = hash_helper.encrypt(user.password)
    return await User(**user.dict()).create()


@router.post("/user_details", response_model=UserDetails)
async def user_detail(user: User = Depends(get_current_user)) -> UserDetails:
    """
    User details route.
    """
    user_details = await get_user_detail(user_id=PydanticObjectId(user.id))
    return UserDetails(**user_details)
