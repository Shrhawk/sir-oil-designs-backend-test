from fastapi import HTTPException, Request, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from models.users_model import User
from .jwt_handler import decode_jwt


async def verify_jwt(jwt_token: str) -> bool:
    """
    Verify JWT token.
    """
    is_token_valid: bool = False
    payload = await decode_jwt(jwt_token)
    if payload:
        is_token_valid = True
    return is_token_valid


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication token"
                )
            if not await verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token"
                )
            return credentials.credentials
        raise HTTPException(status_code=403, detail="Invalid authorization token")


async def get_current_user(token: str = Depends(JWTBearer())) -> User:
    """
    Get current user from token.
    """
    user = await decode_jwt(token)
    return user
