# Johanna Foston 22-SISN-2-036
# Aquí implemento el algoritmo A* desde cero para que el enemigo encuentre el camino al jugador

import heapq

class AStar:
    def __init__(self, mapa):
        self.mapa = mapa

    def heuristica(self, a, b):
        # Uso la distancia Manhattan como heurística
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def buscar(self, inicio, fin):
        # Lista abierta con (costo, nodo)
        abierta = []
        heapq.heappush(abierta, (0, inicio))

        # De dónde vine para reconstruir el camino
        vino_de = {}
        # Costo acumulado para llegar a cada nodo
        costo = {inicio: 0}

        while abierta:
            _, actual = heapq.heappop(abierta)

            # Si llegué al destino reconstruyo el camino
            if actual == fin:
                return self.reconstruir(vino_de, actual)

            # Reviso los vecinos en 4 direcciones
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                vecino = (actual[0] + dr, actual[1] + dc)

                # Me salto si es una pared
                if self.mapa.es_pared(vecino[0], vecino[1]):
                    continue

                nuevo_costo = costo[actual] + 1

                if vecino not in costo or nuevo_costo < costo[vecino]:
                    costo[vecino] = nuevo_costo
                    prioridad = nuevo_costo + self.heuristica(vecino, fin)
                    heapq.heappush(abierta, (prioridad, vecino))
                    vino_de[vecino] = actual

        return []  # No encontré camino

    def reconstruir(self, vino_de, actual):
        # Reconstruyo el camino desde el fin hasta el inicio
        camino = []
        while actual in vino_de:
            camino.append(actual)
            actual = vino_de[actual]
        camino.reverse()
        return camino