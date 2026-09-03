import psycopg2
    
try: 
    conn = psycopg2.connect('postgresql://postgres:pwd@localhost:port/db_name')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    all_addsress = cursor.fetchall()
    
except Exception as ex: 
    print(f'нет доступа к бд Ошибка:{ex}')
        
