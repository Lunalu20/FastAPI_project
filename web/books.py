from fastapi import APIRouter, Depends
from service import books
from model.books import Book
from typing import List
from data.connection_tools import create_session, session

books_router = APIRouter(prefix='/books')

@books_router.get('/')
def get_all(db_session:session = Depends(create_session))->List[Book]:
    return books.get_all(db_session)

@books_router.get('/{id_book}')
def get_one(id_book:int, db_session:session = Depends(create_session))->Book|str:
    return books.get_one(id_book, db_session)

#пост запрос
@books_router.post('')
def create_one(book:Book, db_session:session = Depends(create_session))->Book|str:
    return books.create_book(db_session, book)

#пут запрос
@books_router.put('/{id_book}')
def change_one(id_book:int, book:Book, db_session:session = Depends(create_session))->Book| str:
    return books.update_book(db_session, book, id_book)
print(change_one)

@books_router.patch('/{id_book}')
def patch_one(id_book:int, book:Book, db_session:session = Depends(create_session))->Book| str:
    return books.patch_one(db_session, book, id_book)
    
@books_router.delete('/{id_book}')
def delete_one(id_book:int, db_session:session = Depends(create_session)) -> bool:
    result = books.delete_one(db_session, id_book)
    return result