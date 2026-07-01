from fastapi import FastAPI, Depends, Response
import uvicorn

import psycopg2
main_url = '127.0.0.1'
port = 8000

app = FastAPI()

from web.books import books_router
from web.authors import authors_router

app.include_router(books_router)
app.include_router(authors_router)

# @app.get('/books')
# def sum_num():
#     try: 
#         conn = psycopg2.connect('postgresql://postgres:postgres@127.0.0.1:8888/admin')
#         print('коннект есть')
    
#     except: 
#         print('нет доступа к бд')
        
#     cursor = conn.cursor()

#     cursor.execute('SELECT * FROM books')
#     all_addsress = cursor.fetchall()
#     print(all_addsress)
#     return all_addsress    





# @app.put('/{id_user}/{lool}')
# def put_res(id_user:int, data:dict, lool:int):
#     return id_user, data, lool

# @app.get('/')
# def get_all():
#     data = {
#     "Имя": ["Иван", "Анна", "Сергей"],
#     "Возраст": [28, 22, 35],
#     "Профессия": ["Инженер", "Дизайнер", "Программист"]}

#     return data
    
# # @app.get('/about')
# # def get_info():
# #     return "Информационная страница. По всем вопросам обращаться по номеру: 8-800-555-35-35"

# # @app.get('/{some_body}, {some_body}')
# # def get_somebody(some_body):
# #     return f"Привет {some_body}!"

# @app.get('/sum_num')
# def sum_num(a:int, b:int):
#     res_sum = a+b
#     return f"Сложила число {a} и {b}, получила {res_sum}"

# @app.get('/sub_num')
# def sum_num(a:int, b:int):
#     res_sum = a-b
#     return f"Разность чисел {a} и {b}, получила {res_sum}"

# @app.post('/send_json')
# def send_json (a:dict):
#     return a

# @app.get('/send_json_get')
# def send_json (a:dict):
#     return a
# @app.post('/hello')
# def get_somebody_post(some_body):
#     return f"Привет {some_body}!"

# @app.get('/')
# def get_something(some_body):
#     return "Привет уродец"

# @app.post('/calculate')
# def multiplay_values(a:int, b:int):
#     res = a**b
#     return f"Возвел число {a} в степень {b}: {res}"

# def check_user(user: dict):
#     if len(user['pwd']) < 5:
#         return 'Не верный пароль'
#     return user 
# @app.post('/user')
# def get_user(user : dict = Depends(check_user)):
#     return user

# def admin_checker(user:dict):
#     if user['username']!= 'admin':
#         print('This is not admin')
#         return 'This is not admin'
#     return user

# @app.post('/cheak_admin')
# def check_admin(user:dict = Depends(admin_checker)):
#     return user

if __name__ == '__main__':
    uvicorn.run(
        app,
        host = '127.0.0.1',
        port = 8000
    )