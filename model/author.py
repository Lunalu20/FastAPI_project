from pydantic import BaseModel, Field

class Author(BaseModel):
    id:int = Field(
        default=None,
        title="id", 
        description="Идентификатор"
    )
    fio:str = Field(
        default=None,
        title="fio", 
        description="ФИО автора"
    )
    gender:str = Field(
        default=None,
        title="gender", 
        description="Гендер автора"
    )
    alive:bool = Field(
        default=None,
        title="alive", 
        description="Биологический статус"
    )
    country_code:str = Field(
        default=None,
        title="country_code", 
        description="Страна автора"
    )