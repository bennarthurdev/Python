import sqlite3 
from contextlib import closing 
dados = [
    ('label1' , 'value1'),
    ('label2' , 'value2'),
    ('label3' , 'value3'),
    ('label4' , 'value4'),
]
with sqlite3.connect('newbase.db') as conn:
    conn.row_factory = sqlite3.Row
    with closing(conn.cursor()) as cursor:
        #cursor.execute(f'''
        #    CREATE TABLE newtable (field1 , field2)
        #''')
        cursor.executemany(f'''
            INSERT INTO newtable (field1 , field2)
             VALUES (?, ?)
        ''',dados)
        conn.commit()
        
        for registro in cursor.execute(f'''SELECT * FROM newtable'''):
            print(f"{registro['field1']} , {registro['field2']} ")