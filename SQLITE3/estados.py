import sqlite3 
from contextlib import closing

dados = [['São Paulo' , 4234234] , ['Paraíba' , 1232131231] , ['Pernambuco' , 12321321312312] , ['Rio de Janeiro' , 213321312]]

with sqlite3.connect('estados.db') as conn:
    conn.row_factory = sqlite3.Row
    print(f'{"Id"} {"Estado"} , {"Populacao"}')
    print("=" * 37)
    resultado = conn.execute("SELECT * FROM estados ORDER BY id DESC")
    for estado in resultado:
        print(f'''
        {estado['id']}
        {estado['nome']}
        {estado['populacao']}
        ''')