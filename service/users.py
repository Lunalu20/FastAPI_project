from data import users
from fastapi import HTTPException

def get_all_user(db_session):
    return users.get_all_user(db_session)