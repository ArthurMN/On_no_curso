from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("tela1.html")

@app.route('/tela2' , methods = ['GET', 'POST'])
def register_page():
    return render_template("tela2.html")

@app.route('/tela3')
def feed():
    return render_template("tela3.html")

@app.route('/tela4')
def publication_effected():
    return render_template("tela4.html")
    

if __name__ == "__main__":
    app.run(debug=True)