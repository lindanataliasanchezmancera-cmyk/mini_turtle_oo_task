class Tortuga:
    # Definición de la clase Tortuga

    def __init__(self):
        # Constructor de la clase
        # Se ejecuta cada vez que se crea una nueva tortuga
        self.posicion_x = 0
        # Guarda la posición horizontal inicial de la tortuga

    def adelante(self, camina_adelante):
        # Método para mover la tortuga hacia adelante
        print((" " * self.posicion_x) + "→" + ("-" * camina_adelante) + "↓")
        # Imprime el movimiento usando texto

        self.posicion_x += camina_adelante + 1
        # Actualiza la posición después de avanzar

    def abajo(self, camina_abajo):
        # Método para mover la tortuga hacia abajo
        for _ in range(camina_abajo):
            print((" " * self.posicion_x) + "|")
            # Imprime líneas verticales según la posición actual

    def reiniciar(self):
        # Método para reiniciar la posición de la tortuga
        self.posicion_x = 0
        # La tortuga vuelve a la posición inicial
