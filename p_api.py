import requests
import psycopg2
main_url = '127.0.0.1'
port = 8000

# main_page = requests.post(f"http://{main_url}:{port}/calculate?a={xml_form['a']}&b={xml_form['b']}")
# print('post запрос', main_page.json())

##получаем все книги из беде через рест
# xyi = requests.get(f"http://{main_url}:{port}/books")
# print('get_запрос_все_книги', xyi.json())



# res_sum = {'a': 1500, 'b': 3500}

# xyi = requests.get(f"http://{main_url}:{port}/sum_num?a={res_sum['a']}&b={res_sum['b']}")
# print('get_запрос_сложение', xyi.json())

# xyi = requests.get(f"http://{main_url}:{port}/sub_num?a={res_sum['a']}&b={res_sum['b']}")   
# print('get_запрос_вычитание', xyi.json())

# alina_json = { 'NAME' : 'ALINA',
#               'SERNAME' : 'DAVLYATSHINA'}

# books = requests.get(f"http://{main_url}:{port}/send_json_get", json=all_addsress)
# print('Список классической литературы', books.json())

# books = requests.post(f"http://{main_url}:{port}/send_json", json=all_addsress)
# print('Список классической литературы', books.json())

# xyi = requests.post(f"http://{main_url}:{port}/send_json", json=all_addsress)
# print('json', xyi.json())

# nums = {'a': 5, 'b': 4}
# print(f"http://{main_url}:{port}/calculate?a={nums['a']}&b={nums['b']}")
# main_page = requests.post(f"http://{main_url}:{port}/calculate?a={nums['a']}&b={nums['b']}")
# print('post запрос', main_page.json())

# main_page = requests.get(f"http://{main_url}:{port}/")
# print('get запрос', main_page.json())

# #передача json 
# user_data = {
#     'username' : 'Alinan',
#     'pwd' : 'ilov'
    
# }

# post_data = requests.post(f"http://{main_url}:{port}/cheak_admin", json=user_data)
# print('Пример страницы пользователя', post_data.json())

# post_data = requests.post(f"http://{main_url}:{port}/user", json=user_data)
# print('Пример страницы пользоватея', post_data.json())

# print(user_data['pwd'])
# print(len(user_data['pvd']))

# # #передача json 
# user_data = {
#     "id": 6,
#     "name": 'alina',
#     "author": 'alina'
# }


post_data = {
    "id": None,
    "name": 'may',
    "author": 'may',

}

res = requests.patch(f"http://{main_url}:{port}/books/8", json=post_data)

print(res.json())

# post_data = requests.post(f"http://{main_url}:{port}/books", json=user_data)
# print('Пример создания одной книжки', post_data.json())

# post_data = requests.put(f"http://{main_url}:{port}/books/7", json=user_data)
# print('Пример обновления одной книжки', post_data)
# print(post_data.text)
# id_val = 100
# post_data = requests.delete(f"http://{main_url}:{port}/books/{id_val}")
# print(post_data.text)