from flask import Flask
from flask import render_template
from avatar.control import obtener_planetas

app = Flask(__name__)

@app.route("/")
def home():
    lista_planetas = obtener_planetas()
    return render_template("index.html",
                           name="index",
                           lista_planetas = lista_planetas)

@app.route("/planeta/{numero_planeta}")
def planeta_residentes():
    info_residente = obtener_residentes(numero_planeta)
    return render_template("planeta_residentes.html",
                           name="residente",
                           info_residente = info_residente)

if __name__ == "__main__":
    app.run(debug=True)
