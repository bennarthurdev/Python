import sqlite3
from contextlib import closing as withclose
#CRIA TABELA
#dados = [
  #  ("Nilo", "7788-1432"),
 #   ("André" , "9129-2191"),
   #("Lucas", "2932-12032")
#]
#with sqlite3.connect("base_of_data.db") as conexion:
 #   with withclose(conexion.cursor()) as cursor:
  #      cursor.execute('''
   #         CREATE TABLE agenda (nome text, telefone text)
#
 #       ''')
  #      cursor.executemany('''
   #         INSERT INTO agenda (nome, telefone)
    #        values(? , ?)
     #   ''', dados)
#conexion.commit()
#cursor.close()
#conexion.close()
#FAZCONSULTA
with sqlite3.connect("base_of_data.db") as conexion:
    with withclose(conexion.cursor()) as cursor:
        cursor.execute(""" select * from agenda where nome = "Nilo" """)
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
        print(f'Nome: {resultado[0]}\nTelefone:{resultado[1]}')