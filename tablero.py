from colored import fg, attr  # importa funciones para colorizar texto en consola

class Tablero:
    colores = {
        "r": fg("red"),      # rojo
        "g": fg("green"),   # verde
        "y": fg("yellow"),  # amarillo
        "b": fg("blue")     # azul
    }

    def __init__(self):
        self.turnos = []  # lista para almacenar los intentos y retroalimentacion
        self.adivina_col = []  # lista para almacenar el codigo a adivinar

    def def_color(self, color):
        self.adivina_col = color  # establece el codigo a adivinar

    def color_a_comprobar(self, intento):
        retroalimentar = []  # lista para almacenar la retroalimentacion
        copiar_color = self.adivina_col.copy()  # copia del codigo a adivinar
        for elemento in range(4):
            if intento[elemento] == copiar_color[elemento]:
                retroalimentar.append("color_verde")  # color correcto y en la posicion correcta
                copiar_color[elemento] = None  # marca el color como comprobado
            elif intento[elemento] in copiar_color:
                retroalimentar.append("color_amarillo")  # color correcto pero en la posicion incorrecta
                copiar_color[copiar_color.index(intento[elemento])] = None  # marca el color como comprobado
            else:
                retroalimentar.append("color_blanco")  # color no presente en el codigo
        return retroalimentar  # devuelve la retroalimentacion

    def sh_tabla(self):
        for intento, retroalimentar in self.turnos:  # recorre los intentos y la retroalimentacion
            # muestra el intento usando colores
            intento_jugado = "".join([self.colores[color_jugado] + "o" + attr('reset') for color_jugado in intento])
            # muestra la retroalimentacion usando colores
            retroalimentar_jugada = "".join([
                fg(2) + "O" + attr("reset") if retro_adivina == "color_verde"
                else fg(3) + "O" + attr("reset") if retro_adivina == "color_amarillo"
                else "O"
                for retro_adivina in retroalimentar
            ])
            print(f"{intento_jugado} | {retroalimentar_jugada}")  # imprime el intento y la retroalimentacion

    def actualizar_tabla(self, intento, retroalimentacion):
        self.turnos.append((intento, retroalimentacion))  # agrega un nuevo intento y su retroalimentacion a la lista
