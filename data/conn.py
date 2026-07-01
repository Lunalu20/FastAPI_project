import psycopg2
    
try: 
    conn = psycopg2.connect('postgresql://postgres:1@127.0.0.1:8888/admin')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    all_addsress = cursor.fetchall()
    print(all_addsress)
    print('коннект есть')
    
except Exception as ex: 
    print(f'нет доступа к бд Ошибка:{ex}')
        
