from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from data.books import init_books_query
from data.autors import init_autors_query
from data.users import init_user_query

#создаем параметры для коннекта к бд (вывести в файлы config.json и в дальнейшем читать из него, пароль зашифровать)
host = 'localhost'
port = 1234
user = 'your_username'
pwd = 'your_password'
db_name = 'your_db_name'

db_uri = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db_name}"
store_engine = create_engine(db_uri)

session = sessionmaker(store_engine)

def create_session():
    """ Создаем сессию для подключения к бд"""
    with session() as db:
        try:
            return db
        except Exception as ex:
            print(f'Ошибка подключения к бд: {ex}')
        finally: 
            db.close()
            
            
def init_db_tables():
    """Иницилизация(создание таблиц)"""
    db = create_session()
    db.execute(text(init_books_query))
    db.execute(text(init_autors_query))
    db.execute(text(init_user_query))
    db.commit()
    
if __name__ == '__main__':
    init_db_tables()