from pydantic import BaseModel

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disabled: bool | None = None
    admin: bool | None = None
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserInDB(User):
    hashed_password: str