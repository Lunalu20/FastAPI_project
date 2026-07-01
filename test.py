# UPDATE table_name
# SET column1 = value1, column2 = value2
# WHERE condition;

# table_name = ''
# id_val = 1
# vals_to_update = ''

# main_col = 'id'

# coming_json = {
#     "id":2,
#     "gengre": "comedy",
#     "year": 2015,
#     "language": "ru"
# }

# # print(coming_json["language"])


# for key in coming_json:
#     if key != main_col:
#         vals_to_update += f'{key} = {coming_json[key]}, '
# print(vals_to_update)


# example = f"""
#     UPDATE {table_name}
#     SET 
#         {vals_to_update}
# #     WHERE id = {id_val}
# """

# # print(example)

# #insert example 
# # TABLE_NAME = 'Alina'

# # main_col = 'id'
# # id_va = 1
# # update_tuple = []
# # columns_tuple = []

# # info_alina = {
# #     "year":2001,
# #     "month": 'september',
# #     "genre": 'woman',
# #     "alive": 'yes'
# # }

# # INSERT INTO users (name, email, role) 
# # VALUES ('Alice Smith', 'alice@example.com', 'admin');

# # for key in info_alina:
# #     if key != id:
# #         update += f'{info_alina[key]}, ' 

import requests
main_url = '127.0.0.1'
port = 8000
url = (f"http://{main_url}:{port}/")
print(url)

# main_page = requests.post(f"http://{main_url}:{port}/calculate?a={xml_form['a']}&b={xml_form['b']}")
# print('post запрос', main_page.json())

coming_json = {
    "id":2,
    "gengre": "comedy",
    "year": 2015,
    "language": "ru"
}

# id_book = 6

post_data = requests.put('/{id_book}')