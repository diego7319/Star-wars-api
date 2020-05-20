import json
import requests
from .objetos.Planeta import planeta_obj


REST_PLANETAS = "https://swapi.dev/api/planets/"


def obtener_planetas():
    lista_planetas = []
    #Api de multiples paginas
    siguiente_pagina = REST_PLANETAS
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
                                    _limpiar_vacio(json_planeta["url"]),
                                    _limpiar_vacio(json_planeta["gravity"]))
            lista_planetas.append(nuevo_planeta)
    return lista_planetas


def obtener_residentes(planeta_url):
    lista_planetas = []
    #Api de multiples paginas
    siguiente_pagina = REST_PLANETAS
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
                                    _obtener_num_planeta(json_planeta["url"]),
                                    _limpiar_vacio(json_planeta["gravity"]))
            lista_planetas.append(nuevo_planeta)
    return lista_planetas

def _limpiar_vacio(dato):
    if dato == "N/A" or dato == "unknown":
        return "Dato Desconocido"
    else:
        return dato

def _obtener_num_planeta(dato):
    dato_len=len(dato)
    numero_planeta = numero_planeta[29:dato_len-1]
    print(numero_planeta)
    return numero_planeta
