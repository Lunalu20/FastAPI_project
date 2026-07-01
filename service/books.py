from fake.db.books import fake_books_bd_table
from data import books
from fastapi import HTTPException


def get_all(db_session):
    return books.get_all(db_session)

def get_one(id_book, db_session):
    try:
        found_book = books.get_one(id_book, db_session)
        if found_book:
            return found_book
    except Exception as ex:
        print(ex)
    raise HTTPException(status_code=404, detail=f"Элемент {id_book} не найден")

def create_book(db_session, book):
    book_validated = book.dict()
    book_bd = books.create_book(book_validated, db_session)
    return book_bd

def update_book(db_session, book, id_book:int):
    update_validated = book.dict()
    update_bd = books.update(id_book, update_validated, db_session)
    return update_bd

def change_one(id_book):
    for curr_book in fake_books_bd_table:
        if id_book == curr_book.id:
            return curr_book
    raise HTTPException(status_code=404, detail=f"Элемент {id_book} не найден")

def patch_one(db_session, book, id_book):
    update_validated = book.dict()
    update_bd = books.patch(id_book, update_validated, db_session)
    print("я тут")
    return update_bd


def delete_one(db_session, id_book)->bool:
    update_bd = books.delete(db_session, id_book)
    if not update_bd:
        raise HTTPException(status_code=404, detail=f"Элемент {id_book} не найден")
    return update_bd
    