from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int | None = Field(
        default=None,
        title="id", 
        description="Идентификатор книги"
    )
    name: str | None = Field(
        title="name", 
        description="Название книги"
    )
    author: str | None = Field(
        default=None,
        title="author", 
        description="Автор книги"
    )
    genre: str | None =  Field(
        default=None,
        title="genre", 
        description="Жанр книги"
    )
    language: str | None = Field(
        default=None,
        title="language", 
        description="Язык произведения"
    )
    year: int | None = Field(
        default=None,
        title="year", 
        description="Год выпуска"
    )
    price_in_ru: int | None = Field(
        default=None,
        title="price_in_ru", 
        description="Цена"
    )
    count_page: int | None = Field(
        default=None,
        title="count_page", 
        description="Количество страниц"
    )