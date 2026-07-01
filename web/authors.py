from fastapi import APIRouter
from service import authors
from model.author import Author
from typing import List

authors_router = APIRouter(prefix='/authors')

@authors_router.get('/')
def get_all()->List[Author]:
    return authors.get_all()

@authors_router.get('/{id_author}')
def get_one(id_author:int)->Author|str:
    return authors.get_one(id_author)

@authors_router.put('/{id_author}')
def put_one(id_author:int)->Author|str:
    return authors.put_one(id_author)

@authors_router.patch('/{id_author}')
def patch_one(id_author:int)->Author|str:
    return authors.patch_one(id_author)

@authors_router.delete('/{id_author}')
def delete_one(id_author:int)->Author|str:
    return authors.delete_one(id_author)