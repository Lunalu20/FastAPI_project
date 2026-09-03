from model.books import Book

fake_books_bd_table = [
    Book(
        id = 1,
        name = 'Преступление и наказание',
        author = 'Ф.М. Достоевский',
        genre = 'Русская классика',
        language = 'русский',
        year = 1849,
        price_in_ru = 500,
        count_page = 200
    ),
    Book(
        id = 2,
        name = 'Время жить и умирать',
        author = 'Э.М.Ремарк',
        genre = 'Роман',
        language = 'русский',
        year = 1980,
        price_in_ru = 1000,
        count_page = 450
    ),
    Book(
        id = 3,
        name = 'Финансист',
        author = 'Теодор Драйзер',
        genre = 'Роман',
        language = 'русский',
        year = 2008,
        price_in_ru = 153,
        count_page = 603
    ),
    Book(
        id = 4,
        name = 'Атомные привычки',
        author = 'Джеймс клир',
        genre = 'инфо-циганство',
        language = 'английский',
        year = 2026,
        price_in_ru = 700,
        count_page = 351
    ),        
     Book(
        id = 5,
        name = 'Норвежский лес',
        author = 'Харуки Мураками',
        genre = 'драма',
        language = 'японский',
        year = 2016,
        price_in_ru = 1500,
        count_page = 340
    ),
]

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$iVR61sr0mVZ+4ikCBL60HQ$YzVLrROJOWX19ND0PnKKRF13W/b8dqcKxDNHE2MPAHU",
        "admin": True,
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}