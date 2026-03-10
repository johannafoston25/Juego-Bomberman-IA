# Johanna Foston 22-SISN-2-036
# Aquí implemento el árbol de comportamiento desde cero para controlar al enemigo

# Estados posibles del árbol
EXITO = "EXITO"
FALLO = "FALLO"
CORRIENDO = "CORRIENDO"

class Nodo:
    def ejecutar(self, enemigo, jugador, mapa, bombas):
        pass

# Nodos de control 

class Secuencia(Nodo):
    # Ejecuta los hijos en orden, si uno falla para todo
    def __init__(self, hijos):
        self.hijos = hijos

    def ejecutar(self, enemigo, jugador, mapa, bombas):
        for hijo in self.hijos:
            resultado = hijo.ejecutar(enemigo, jugador, mapa, bombas)
            if resultado == FALLO:
                return FALLO
        return EXITO

class Selector(Nodo):
    # Ejecuta los hijos en orden, si uno tiene éxito para
    def __init__(self, hijos):
        self.hijos = hijos

    def ejecutar(self, enemigo, jugador, mapa, bombas):
        for hijo in self.hijos:
            resultado = hijo.ejecutar(enemigo, jugador, mapa, bombas)
            if resultado == EXITO:
                return EXITO
        return FALLO

# Nodos de acción

class HuirDeBomba(Nodo):
    # Me alejo si hay una bomba cerca
    def ejecutar(self, enemigo, jugador, mapa, bombas):
        for bomba in bombas:
            dist = abs(enemigo.row - bomba.row) + abs(enemigo.col - bomba.col)
            if dist <= 3:
                enemigo.huir_de_bomba(bomba, mapa)
                return EXITO
        return FALLO

class PerseguirJugador(Nodo):
    # Persigo al jugador usando A*
    def ejecutar(self, enemigo, jugador, mapa, bombas):
        enemigo.perseguir(jugador, mapa)
        return EXITO

class Patrullar(Nodo):
    # Me muevo aleatoriamente si no pasa nada
    def ejecutar(self, enemigo, jugador, mapa, bombas):
        enemigo.patrullar(mapa)
        return EXITO

class ArbolComportamiento:
    def __init__(self):
        # Primero huyo de bombas, luego persigo, luego patrullo
        self.raiz = Selector([
            HuirDeBomba(),
            PerseguirJugador(),
            Patrullar()
        ])

    def ejecutar(self, enemigo, jugador, mapa, bombas):
        self.raiz.ejecutar(enemigo, jugador, mapa, bombas)