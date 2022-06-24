import sqlite3
from contextlib import closing

class outdata_class:
    def __init__(self):
        print("Funcionando!")
    def makeconnection():
        with sqlite3.connect() as conn:
            with closing(conn.cursor()) as cursor:
                
                conn.commit()
    def add_one(first, last, email):
        cursor.execute()