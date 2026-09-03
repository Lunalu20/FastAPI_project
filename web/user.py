from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from model.users import User, UserInDB
from auth.fast_api_auth import authenticate_user, create_access_token, get_current_active_user, get_session, get_user, check_admin
from typing import Annotated
from model.users import Token
from data.connection_tools import create_session, session
from auth import fast_api_auth
from data import users

ACCESS_TOKEN_EXPIRE_MINUTES = 30

auth_router = APIRouter(prefix='/auth')

@auth_router.post("/token")
async def login_for_access_token(result_in_bd: Annotated[dict, Depends(get_session)],
                                 form_data: Annotated[OAuth2PasswordRequestForm, Depends()],) -> Token:
    user = authenticate_user(result_in_bd, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}, 
        )
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expire
    )
    return Token(access_token=access_token, token_type="bearer")

@auth_router.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    return current_user

@auth_router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"items_id": "Foo", "owner": current_user.username}]

@auth_router.get("/all_users")
async def get_all_users(result_in_bd: Annotated[User, Depends(check_admin)], db_session: Annotated [session, Depends(create_session)]):
    return users.get_all_users(db_session)

@auth_router.post("/create_user")
async def create_user(user:UserInDB, check: Annotated[User, Depends(check_admin)], db_session: Annotated [session, Depends(create_session)])-> User|str:
    result = await fast_api_auth.create_user(user, db_session)
    return result

@auth_router.put("/change_password")
async def change_password(user:UserInDB, db_session: Annotated [session, Depends(create_session)], check: Annotated[bool, Depends(check_admin)]):
    result = await fast_api_auth.change_password(user, db_session)
    return result

@auth_router.delete("/delete_user")
async def delete_user(user:User, check: Annotated[User, Depends(check_admin)], db_session: Annotated [session, Depends(create_session)])-> User|str:
    result = await fast_api_auth.delete_user(user, db_session)
    return result
    
    