import sqlite3
import os
from sys import path

ROOT = os.path.dirname(os.path.realpath(__file__))

def create_course(nome_curso, nome_facilitador, preco, data, link, validacao):
    con = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("""insert into cursos (nome_curso, nome_facilitador, preco, data, link,  validacao) 
                values(?,?,?,?,?,?)""", 
                (nome_curso, nome_facilitador, preco, data, link, validacao))
    con.commit()
    con.close()
    
def get_course():
    con = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("SELECT * FROM cursos")
