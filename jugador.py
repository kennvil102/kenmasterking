import random  # importa modulo random  

class Jugador:  # clase base para jugadores
    colores = ["r", "g", "y", "b"]  # colores disponibles
    
    def __init__(self, el_jugador=True):  # inicializa jugador
        self.el_jugador = el_jugador  # indica si es humano (True) o IA (False)

class Creador(Jugador):  # clase para crear codigo de colores
    def crea_codigo(self):  # metodo para crear codigo
        if self.el_jugador:  # si es humano
            # solicita codigo de colores
            cod_color = input("Ingrese el codigo de colores a crear (ej. r g b y): ").strip().split()
        else:  # si es IA
            # genera codigo aleatorio
            cod_color = random.choices(self.colores, k=4)
        return cod_color  # devuelve el codigo

class Adivinador(Jugador):  # clase para adivinar codigo de colores
    def adivinar_codigo(self):  # metodo para adivinar codigo
        if self.el_jugador:  # si es humano
            # solicita codigo a adivinar
            cod_codigo = input("Ingrese el codigo de colores a adivinar (ej. r g b y): ").strip().split()
        else:  # si es IA
            # genera codigo aleatorio
            cod_codigo = random.choices(self.colores, k=4)
        return cod_codigo  # devuelve el codigo adivinado
