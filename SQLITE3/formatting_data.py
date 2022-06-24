import sqlite3 # to work with data-base model, modules
from contextlib import closing #to work with cursor
dados = [
    ('label1' , 'value1'),
    ('label2' , 'value2'),
    ('label3' , 'value3'),
    ('label4' , 'value4'),
]
id_request = int(input('Chose a user by id:'))
with sqlite3.connect('base_of_data.db') as conn:
    with closing(conn.cursor()) as cursor:
        #cursor.execute('CREATE TABLE newtable (field1 , field2)')
        cursor.executemany(
        f'''
        INSERT INTO newtable (field1, field2) 
        values (?, ?)
        ''' , dados)

        conn.commit()
        cursor.execute('SELECT rowid, * FROM newtable')
        print('Commited changes')
        itens = cursor.fetchall()
        print(f'See this awesome data visualization! \n')
        for item in itens:
            if item[0] == id_request:
                print(item[2])