from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira ppagina do site
    # route -> hashtagtreinamento.com/contatos
    # função-> o que você quer exibir naquela página
@app.route("/") 
def homepage():
    return render_template('homepage.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/inscrito/<nome_inscrito>')
def inscrito(nome_inscrito):
    return f'Olá {nome_inscrito}' 

@app.route("/hello") 
def hello():
    return render_template('hello.html')

@app.route("/index") 
def index():
    return render_template('index.html')

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)