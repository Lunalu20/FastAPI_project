from model.books import Book
from typing import List
from sqlalchemy import text


DB_INIT_SCHEMA_NAME = 'public'
DB_INIT_TABLE_NAME = 'books'
MAIN_COL = 'id'

init_books_query = f"""
    CREATE TABLE IF NOT EXISTS {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME}(
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        name varchar(512),
        author varchar(512),
        genre varchar(512), 
        language varchar(512),
        year varchar(512),
        price_in_ru int, 
        count_page int
    )
    """
    
def get_all(db_session)->List[Book]:
    """получаем все книги"""
    query = """
    SELECT id, name, author, genre, language, year, price_in_ru, count_page
    FROM {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME};
    """
    res = db_session.execute(text(query))
    
    all_books = res.all()
    cols = list(res.keys())
    all_books_dicted = [dict(zip(cols, row)) for row in all_books]
    
    validates_books = []
    for book in all_books_dicted:
        validates_books.append(Book(**book))
    return validates_books
        
        
def get_one(res_json, db_session):
    """получаем конкретную книгу"""
    
    query = f"""
        SELECT id, name, author, genre, language, year, price_in_ru, count_page
        FROM {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME}
        WHERE id = {id}
    """
    
    res = db_session.execute(text(query))
    
    all_books = res.all()
    cols = list(res.keys())
    all_books_dicted = [dict(zip(cols,row)) for row in all_books]
    
    return Book(**all_books_dicted[0])


def create_book(book:dict, db_session):
    """создаем книгу"""
    res_json_param = []
    res_json = []
    
    for key in book:
        if key != MAIN_COL:
            res_json.append(key)
            res_json_param.append(book[key])

    query = f"""
       INSERT INTO {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME} ({', '.join(f'"{item}"' for item in res_json)})
       VALUES {tuple(res_json_param)}
    """
    
    res = db_session.execute(text(query))
    db_session.commit()
    
    return Book(**book)  

def update(id_book:int, book:dict, db_session):
    """обновляем данные книги"""
    update_json = ''
    
    for key in book:
        if key != MAIN_COL:
            update_json += f"{key} = '{book[key]}', "
    update_json = update_json[:-2]
    print(update_json)
            
    query = f"""
        UPDATE {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME}
        SET {update_json}
        WHERE id = {id_book}
    """
    res = db_session.execute(text(query))
    db_session.commit()
    
    return Book(**book)

def patch(id_book, book, db_session):
    patch_key = ''
    # patch_ful = ''
    for key in book:
        if key != MAIN_COL and book[key] != None:
            patch_key += f"{key} = '{book[key]}', "
    patch_key = patch_key[:-2]
    query = f"""
    UPDATE {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME}
    SET {patch_key}
    WHERE id = {id_book}
    """
    res = db_session.execute(text(query))
    db_session.commit()
        
    return Book(**book)
        
def delete(db_session, id_book:int):
    """Удаляем книгу"""
    
    query = f"""
        SELECT id, name, author, genre, language, year, price_in_ru, count_page
        FROM {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME}
        WHERE id = {id_book}
    """
    
    res = db_session.execute(text(query))
    
    all_books = res.all()
    print(f'мы тут {all_books}')
    
    if not all_books:
        return False
    else:
        query = f"""
        DELETE FROM {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME}
        WHERE id = {id_book}
        """
    res = db_session.execute(text(query))
    db_session.commit()
    return True