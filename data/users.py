from typing import List
from sqlalchemy import text
from pydantic import BaseModel
from model.users import User

DB_INIT_SCHEMA_NAME_USER = 'public'
DB_INIT_TABLE_NAME_USER = 'users'
    
init_user_query = f"""
    CREATE TABLE IF NOT EXISTS {DB_INIT_SCHEMA_NAME_USER}.{DB_INIT_TABLE_NAME_USER}(
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        username varchar(512),
        hashed_password varchar(1024),
        email varchar(512),
        full_name varchar(512), 
        disabled BOOLEAN,
        admin BOOLEAN
    )
    """

def get_all_users(db_session)->List[User]:
    
    query = f"""
    SELECT id, username, hashed_password, email, full_name, disabled, admin
	FROM {DB_INIT_SCHEMA_NAME_USER}.{DB_INIT_TABLE_NAME_USER}
    """
    res = db_session.execute(text(query))  
    all_users = res.all()
    user_list = list(res.keys())
    user_to_dict = [dict(zip(user_list, row)) for row in all_users]
    return user_to_dict


async def create_user(user_validated, db_session):
    column = str(tuple(user_validated.keys())).replace("'", '"')
    values = tuple(user_validated.values())
    query = f"""
       INSERT INTO {DB_INIT_SCHEMA_NAME_USER}.{DB_INIT_TABLE_NAME_USER} {column}
       VALUES {values}
    """
    db_session.execute(text(query))
    db_session.commit()
    return f"Пользователь успешно добавлен {user_validated}"

async def change_password(password_hash, email_to_change, db_session):
    query = f"""
    UPDATE {DB_INIT_SCHEMA_NAME_USER}.{DB_INIT_TABLE_NAME_USER}  
	SET hashed_password = '{password_hash}'
	WHERE email = '{email_to_change}';
    """
    db_session.execute(text(query))
    db_session.commit()
    return f"Пароль обновлен: {password_hash}"

async def delete_user(user_email, db_session):
    query = f"""
    DELETE FROM {DB_INIT_SCHEMA_NAME_USER}.{DB_INIT_TABLE_NAME_USER}
	WHERE email = '{user_email}';
    """ 
    db_session.execute(text(query))
    db_session.commit()
    return f"Пользователь с {user_email} удален!"