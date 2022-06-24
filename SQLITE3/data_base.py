from contextlib import closing as withclose
#from mailbox import NotEmptyError
import sqlite3
#from tkinter import N
bool_control = True
while bool_control:
    inputdata_name = input("Type a name to put on data_base:")
    inputdata_value = input("Type the price for this product:")
    inputdata = (inputdata_name, inputdata_value)
    question = input("You want continue [Y/N]")
    if question == 'Y':
        bool_control = False

nome = input("Type a name for search in data_base:")

with sqlite3.connect('precos.db') as conexion:
    with withclose(conexion.cursor()) as cursor:
        cursor.executemany(f'insert into precos  {inputdata}')#put user datas on data_base
        cursor.execute(f'select * from precos where nome = {nome}')
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nothing search in data_base!")
                break
            print(f"Preço {resultado[1]}")
            x += 1