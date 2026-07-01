from fake.db.author import fake_authors_db_table

def get_all():
    return fake_authors_db_table

def get_one(id_author):
    for curr_author in fake_authors_db_table:
        if id_author == curr_author.id:
            return curr_author
    return f"Автор {id_author} не найден!"

def change_one(id_author):
    for curr_author in fake_authors_db_table:
        if id_author == curr_author.id:
            return curr_author
    return f"Автор {id_author} не найден!"

def patch_one(id_author):
    for curr_author in fake_authors_db_table:
        if id_author == curr_author.id:
            return curr_author
    return f"Автор {id_author} не найден!"

def delete_one(id_author):
    for curr_author in fake_authors_db_table:
        if id_author == curr_author.id:
            return curr_author
    return f"Автор {id_author} не найден!"