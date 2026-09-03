from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from data.users import get_all_users
from model.users import User, UserInDB, TokenData
from data.connection_tools import create_session, session
from typing import Annotated
from data import users

SECRET_KEY = "59d42347fd7383dd6a2fccfb95c2bdffe3e822"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

auth_router = APIRouter(prefix='/auth')

def fake_hash_password(password:str)->str:
    return "fakehashed" + password

password_hash = PasswordHash.recommended()
DUMMY_HASH = password_hash.hash("dummypassword")

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password:str)->str:
    return password_hash.hash(password)

def get_session(db_session: Annotated [session, Depends(create_session)]):
    result_bd = get_all_users(db_session)
    return result_bd

def authenticate_user(fake_bd, username: str, password: str):
    user = get_user(fake_bd, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else: 
        expire = datetime.now(timezone.utc + timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_user(result_in_bd: Annotated[list, Depends(get_session)], username:str):
    for db_user in result_in_bd:
        if username == db_user.get('username'): # здесь используем реальную бд
            return UserInDB(**db_user)
                
def fake_decode_token(result_in_bd: Annotated[dict, Depends(get_session)],token):
    user = get_user(result_in_bd, token)
    return user
     
async def get_current_user(result_in_bd: Annotated[dict, Depends(get_session)], token: Annotated[str, Depends(oauth2_scheme)]):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credential",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credential_exception
    user = get_user(result_in_bd, username=token_data.username)
    if user is None:
        raise credential_exception
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="inactive_user")
    return current_user

async def check_admin(check_user: Annotated[User, Depends(get_current_active_user)]):
    if not check_user.admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    return check_user

async def create_user(user, db_session: Annotated [session, Depends(create_session)]):
    user_validated = user.dict().copy()
    for k in user_validated:
        if k == "hashed_password":
            value_password = user_validated[k]
            hashed_password = get_password_hash(value_password)
            user_validated.update({'hashed_password': hashed_password})
            result = await users.create_user(user_validated, db_session)
            return result
        
async def change_password(user, db_session):
    user_dict = user.dict().copy()
    for i in user_dict:
        if i == "email":
            email_to_change = user_dict[i]
            for i in user_dict:
                if i == "hashed_password":
                    password_to_change = user_dict[i]
                    password_hash = get_password_hash(password_to_change)
                    user_dict.update({'hashed_password': password_hash})
                    result = await users.change_password(password_hash, email_to_change, db_session)
                    return result
                
async def delete_user(user, db_session):
    user_dict = user.dict().copy()
    for i in user_dict:
        if i == "email":
            user_email = user_dict[i]
            result = await users.delete_user(user_email, db_session)
            return result
        