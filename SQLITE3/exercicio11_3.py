from distutils.util import execute
import sqlite3 
from contextlib import closing
#
with sqlite3.connect("precos.db") as conn:
    for register in conn.execute("select * from precos_new"):
        print(f"Nome: {register[0]} ")