import json
import requests
from .Modelos import planeta_obj, personaje_obj, pelicula_obj

__all__ = ["obtener_planetas",
           "obtener_peliculas",
           "obtener_personajes",
           "obtener_personajes_por_planeta"]

def obtener_planetas():
    lista_planetas = []
    #Api de multiples paginas
    siguiente_pagina = "https://swapi.dev/api/planets/"
    while siguiente_pagina:
        json_data = json.loads((requests.get(siguiente_pagina)).content)
        siguiente_pagina = json_data["next"]
        for json_planeta in json_data["results"]:
            nuevo_planeta = planeta_obj(_limpiar_vacio(json_planeta["name"]),
                                    _limpiar_vacio(json_planeta["rotation_period"]),
                                    _limpiar_vacio(json_planeta["orbital_period"]),
                                    _limpiar_vacio(json_planeta["diameter"]),
                                    _limpiar_vacio(json_planeta["climate"]),
                                    _limpiar_vacio(json_planeta["terrain"]),
                                    _limpiar_vacio(json_planeta["population"]),
                                    _limpiar_vacio(json_planeta["residents"]),
                                    _obtener_numero_id(json_planeta["url"]),
                                    _limpiar_vacio(json_planeta["gravity"]))
            lista_planetas.append(nuevo_planeta)
    return lista_planetas


def obtener_peliculas():
    lista_peliculas = []
    #Api de multiples paginas
    siguiente_pagina = "https://swapi.dev/api/films/"
    while siguiente_pagina:
        json_data = json.loads((requests.get(siguiente_pagina)).content)
        siguiente_pagina = json_data["next"]
        for json_pelicula in json_data["results"]:
            nueva_pelicula = pelicula_obj(_limpiar_vacio(json_pelicula["title"]),
                                    _limpiar_vacio(json_pelicula["episode_id"]),
                                    _limpiar_vacio(json_pelicula["opening_crawl"]),
                                    _limpiar_vacio(json_pelicula["director"]),
                                    _limpiar_vacio(json_pelicula["producer"]),
                                    _limpiar_vacio(json_pelicula["release_date"]),
                                    _obtener_numero_id(json_pelicula["url"]))
            lista_peliculas.append(nueva_pelicula)
    return lista_peliculas


def obtener_personajes():
    lista_personajes = []
    #Api de multiples paginas
    siguiente_pagina = "https://swapi.dev/api/people/"
    while siguiente_pagina:
        json_data = json.loads((requests.get(siguiente_pagina)).content)
        siguiente_pagina = json_data["next"]
        for personaje_json in json_data["results"]:
                nuevo_personaje = personaje_obj(
                              _limpiar_vacio(personaje_json["name"]),
                              _limpiar_vacio(personaje_json["height"]),
                              _limpiar_vacio(personaje_json["mass"]),
                              _limpiar_vacio(personaje_json["hair_color"]),
                              _limpiar_vacio(personaje_json["skin_color"]),
                              _limpiar_vacio(personaje_json["eye_color"]),
                              _limpiar_vacio(personaje_json["birth_year"]),
                              _limpiar_vacio(personaje_json["gender"]),
                              _obtener_numero_id(personaje_json["url"]))
                lista_personajes.append(nuevo_personaje)
    return lista_personajes

#Obtiene todos los residentes de un planeta
def obtener_personajes_por_planeta(num_planeta):
    dict_personajes = {}
    lista_personajes = []
    api_base = "https://swapi.dev/api/planets/" + str(num_planeta)
    #Api de multiples paginas
    json_data = json.loads((requests.get(api_base)).content)
    dict_personajes["nombre_planeta"] = json_data["name"]
    urls_personajes_de_planeta = json_data["residents"]
    for url_personaje in urls_personajes_de_planeta:
        nuevo_personaje = _obtener_personaje(url_personaje)
        lista_personajes.append(nuevo_personaje)
    dict_personajes["lista_personajes"] = lista_personajes
    return dict_personajes


#UTILS
#Manejo de datos vacios
def _limpiar_vacio(dato):
    if dato == "N/A" or dato == "unknown":
        return "Dato Desconocido"
    else:
        return dato

#obtiene el numero id de una url
def _obtener_numero_id(dato):
    dato_len=len(dato)
    return dato[29:dato_len-1]

#obtiene una clase residente_obj a partir del link json
def _obtener_personaje(personaje_link):
    parsed_res = json.loads((requests.get(personaje_link)).content)
    personaje = personaje_obj(_limpiar_vacio(parsed_res["name"]),
                              _limpiar_vacio(parsed_res["height"]),
                              _limpiar_vacio(parsed_res["mass"]),
                              _limpiar_vacio(parsed_res["hair_color"]),
                              _limpiar_vacio(parsed_res["skin_color"]),
                              _limpiar_vacio(parsed_res["eye_color"]),
                              _limpiar_vacio(parsed_res["birth_year"]),
                              _limpiar_vacio(parsed_res["gender"]),
                              _obtener_numero_id(parsed_res["url"]))
    return personaje
