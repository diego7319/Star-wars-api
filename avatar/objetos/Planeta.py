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
