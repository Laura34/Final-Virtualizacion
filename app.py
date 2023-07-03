from requests import request
from flask import Flask, render_template, request
from BaseDatos import Conexion

db = Conexion()

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    mensaje=''
    if request.method =='POST':
        user = request.form['user']
        password = request.form['password']
        host = request.form['host']
        mensaje = db.conectar(user, password, host)
        return render_template('index.html', mensaje=mensaje)
    return render_template('index.html', mensaje=mensaje)

@app.route('/usuarios')
def usuarios():
    usuarios = db.leerUsuarios()
    return render_template('leer_usuarios.html', usuarios=usuarios)

@app.route('/peliculas')
def peliculas():
    peliculas = db.leerPeliculas()
    return render_template('leer_peliculas.html', peliculas=peliculas)
