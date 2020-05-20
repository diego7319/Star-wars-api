class planeta_obj():
    def __init__(self,
                 nombre_planeta,
                 periodo_rotacional,
                 periodo_orbital,
                 diametro,
                 clima,
                 tipo_terrenos,
                 poblacion,
                 residentes,
                 planeta_url,
                 gravedad):
        self.nombre_planeta = nombre_planeta
        self.periodo_rotacional = periodo_rotacional
        self.periodo_orbital = periodo_orbital
        self.diametro = diametro
        self.clima = clima
        self.tipo_terrenos = tipo_terrenos
        self.poblacion = poblacion
        self.residentes = residentes
        self.planeta_url = planeta_url
        self.gravedad = gravedad

    def __str__(self):
        return self.nombre_planeta


class personaje_obj():
    def __init__(self,
                 nombre,
                 altura,
                 peso,
                 color_cabello,
                 color_piel,
                 eye_color,
                 nacimiento,
                 genero,
                 personaje_url):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.color_cabello = color_cabello
        self.color_piel = color_piel
        self.nacimiento = nacimiento
        self.genero = genero
        self.personaje_url = personaje_url

    def __str__(self):
        return self.nombre


class pelicula_obj():
    def __init__(self,
                 titulo,
                 episodio,
                 mensaje_apertura,
                 director,
                 productor,
                 fecha_estreno,
                 pelicula_url):
        self.titulo = titulo
        self.episodio = episodio
        self.mensaje_apertura = mensaje_apertura
        self.director = director
        self.productor = productor
        self.fecha_estreno = fecha_estreno
        self.pelicula_url = pelicula_url

    def __str__(self):
        return self.titulo
