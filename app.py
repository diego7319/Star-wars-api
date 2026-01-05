from flask import Flask
from flask import render_template
from avatar.control import *
from flask_caching import Cache


cache = Cache(config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp'})
app = Flask(__name__, static_folder='static/')
cache.init_app(app)
timecache= 100

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

@app.route("/planets")
@cache.cached(timeout=timecache)
def planetas():
    titulo = "Star Wars planets"
    lista_planetas = obtener_planetas()
    return render_template("planetas.html",
                           name="planetas",
                           lista_planetas = lista_planetas,
                           titulo = titulo )


@app.route("/movies")
@cache.cached(timeout=timecache)
def peliculas():
    titulo = "Star Wars Movies"
    lista_peliculas = obtener_peliculas()
    return render_template("peliculas.html",
                           name="peliculas",
                           lista_peliculas = lista_peliculas,
                           titulo = titulo)


@app.route("/characters")
@cache.cached(timeout=timecache)
def personajes():
    titulo = "Personajes de Star Wars"
    lista_personajes = obtener_personajes()
    return render_template("personajes.html",
                           name="personajes",
                           lista_personajes = lista_personajes,
                           titulo = titulo)


@app.route("/characters_per_planet/<numero_planeta>")
@cache.cached(timeout=timecache)
def personajes_por_planeta(numero_planeta):
    personajes_por_planeta = obtener_personajes_por_planeta(numero_planeta)
    return render_template("personajes_por_planeta.html",
                            personajes_por_planeta = personajes_por_planeta)

