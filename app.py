
import sqlite3

from werkzeug.utils import redirect
from models import create_course, get_course
from flask import Flask, render_template, url_for, request



app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("tela1.html")

@app.route('/tela2')
def register_page():
    return render_template("tela2.html")

@app.route('/cadastro', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome_curso = request.form.get('nome_curso')
        nome_facilitador = request.form.get('nome_facilitador')
        link = request.form.get('link')
        data =  request.form.get('data')
        preco = request.form.get('preco')
        validacao = request.form.get('validacao')
        create_course(nome_curso, nome_facilitador, preco, data, link, validacao) 
    return redirect(url_for("publication_effected"))


@app.route('/tela3')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM cursos")
    rows = cur.fetchall()
    return render_template("tela3.html", rows = rows)


@app.route('/tela4', methods= ['POST','GET'])
def publication_effected():
    if request.method == 'POST':
        if request.form.get('acao1'):
           return redirect(url_for("homepage"))

        if request.form.get('acao2'):
            return redirect(url_for('register_page'))

    return render_template("tela4.html")
    
if __name__ == "__main__":
    app.run(debug=True)
