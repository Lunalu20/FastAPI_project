DB_INIT_SCHEMA_NAME = 'public'
DB_INIT_TABLE_NAME = 'authors'

init_autors_query = f"""
    CREATE TABLE IF NOT EXISTS {DB_INIT_SCHEMA_NAME}.{DB_INIT_TABLE_NAME}(
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        fio varchar(512),
        gender varchar(512),
        alive bool, 
        country_code varchar(512)
    )
    """