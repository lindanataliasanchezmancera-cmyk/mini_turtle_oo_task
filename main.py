from mini_turtle_oo import Tortuga
# Importo la clase Tortuga desde el paquete

# Crear dos tortugas independientes
t1 = Tortuga()
# Primera tortuga

t2 = Tortuga()
# Segunda tortuga

print("=== Tortuga 1 ===")
# Mensaje para identificar los movimientos de la primera tortuga

t1.adelante(4)
# La tortuga 1 avanza 4 espacios

t1.abajo(2)
# La tortuga 1 baja 2 posiciones

t1.adelante(3)
# La tortuga 1 vuelve a avanzar

t1.abajo(1)
# La tortuga 1 baja una posición

print("\n=== Tortuga 2 ===")
# Mensaje para identificar los movimientos de la segunda tortuga

t2.adelante(2)
# La tortuga 2 avanza menos que la primera

t2.abajo(1)
# La tortuga 2 baja una posición

t2.adelante(6)
# La tortuga 2 avanza más distancia

t2.abajo(1)
# La tortuga 2 baja una posición
