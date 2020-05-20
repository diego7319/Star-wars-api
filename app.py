from flask import Flask
from flask import render_template
from avatar.control import *

app = Flask(__name__, static_folder='static/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/planetas")
def planetas():
    lista_planetas = obtener_planetas()
    return render_template("planetas.html",
                           name="planetas",
                           lista_planetas = lista_planetas)

@app.route("/peliculas")
def peliculas():
    lista_peliculas = obtener_peliculas()
    return render_template("peliculas.html",
                           name="peliculas",
                           lista_peliculas = lista_peliculas)

@app.route("/residentes_de_planeta/<numero_planeta>")
def residentes_por_planeta(numero_planeta):
    residentes_por_planeta = obtener_residentes_por_planeta(numero_planeta)
    return render_template("residentes_por_planeta.html",
                            residentes_por_planeta = residentes_por_planeta)

@app.route("/peliculas_por_residente/<numero_residente>")
def peliculas_por_residente(numero_residente):
    peliculas_por_residentes = obtener_peliculas_por_residente(numero_residente)
    return render_template("peliculas_por_residente.html",
                            peliculas_por_residente = peliculas_por_residente)

if __name__ == "__main__":
    app.run(debug=True)
