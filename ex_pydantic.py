from pydantic import BaseModel

class User(BaseModel):
    username: str
    pwd: str
    
alina = {
    'username': 'Alina',
    'pwd': 'iloveayrat'
}

# a = User(**alina)
a = User(username=alina['username'], pwd=alina['pwd'])
print(a)