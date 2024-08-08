from jugador import Creador, Adivinador  # importa las clases Creador y Adivinador
from tablero import Tablero  # importa la clase Tablero

class Jugar:
    def __init__(self):
        self.tablero = Tablero()  # inicializa el tablero del juego
        self.creador_codigo = None  # almacena al creador del codigo
        self.adivinador_codigo = None  # almacena al adivinador del codigo

    def elegir_rol(self):
        pregunta = input("¿Desea ser el creador o adivinador? c-a: ").lower()  # pregunta el rol al usuario
        if pregunta == "c":
            self.creador_codigo = Creador(True)  # jugador humano como creador
            self.adivinador_codigo = Adivinador(False)  # IA como adivinador
        else:
            self.creador_codigo = Creador(False)  # IA como creador
            self.adivinador_codigo = Adivinador(True)  # jugador humano como adivinador

        self.tablero.def_color(self.creador_codigo.crea_codigo())  # establece el codigo en el tablero

    def jugadas_turnos(self):
        for turnos in range(12):  # permite hasta 12 turnos
            intento = self.adivinador_codigo.adivinar_codigo()  # el adivinador hace un intento
            retroalimentacion = self.tablero.color_a_comprobar(intento)  # obtiene retroalimentacion del intento
            self.tablero.actualizar_tabla(intento, retroalimentacion)  # actualiza la tabla con el intento y la retroalimentacion
            self.tablero.sh_tabla()  # muestra el estado actual de la tabla
            print(turnos)  # imprime el numero de turno
            if retroalimentacion == ["color_verde"] * 4:  # verifica si el codigo es correcto
                print("WIN")  # imprime mensaje de victoria
                return  # termina el juego
        
        print("LOSE")  # imprime mensaje de derrota si no se adivina el codigo

    def iniciar_juego(self):
        self.elegir_rol()  # permite al jugador elegir su rol y establece el codigo
        self.jugadas_turnos()  # inicia el proceso de jugadas y turnos

if __name__ == "__main__":
    juego = Jugar()  # crea una instancia del juego
    juego.iniciar_juego()  # inicia el juego
