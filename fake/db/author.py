from model.author import Author

fake_authors_db_table = [
    Author(
        id = 1,
        fio = 'Ф.М. Достоевский',
        gender = 'мужчина',
        alive = False,
        country_code = 'ru'
    ),
    Author(
        id = 2,
        fio = 'Э.М. Ремарк',
        gender = 'мужчина',
        alive = False,
        country_code = 'germany'
    ),
    Author(
        id = 3,
        fio = 'Теодор Драйзер',
        gender = 'мужчина',
        alive = False,
        country_code = 'england'
    ),
    Author(
        id = 4,
        fio = 'Джеймс Клир',
        gender = 'мужчина',
        alive = False,
        country_code = 'england'
    ),
    Author(
        id = 5,
        fio = 'Харуки Мураками',
        gender = 'мужчина',
        alive = True,
        country_code = 'Japan'
    )
]