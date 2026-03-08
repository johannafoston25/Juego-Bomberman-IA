# Johanna Foston 22-SISN-2-036
import pygame
import random
from scripts.astar import AStar
from scripts.behaviour_tree import ArbolComportamiento

class Enemy:
    def __init__(self, x, y, tile_size):
        self.tile_size = tile_size
        self.col = x // tile_size
        self.row = y // tile_size
        self.x = self.col * tile_size
        self.y = self.row * tile_size
        self.speed = 2
        self.move_timer = 0
        self.move_delay = 500  # se mueve cada 500ms

        # Aquí creo el árbol de comportamiento y el A*
        self.arbol = ArbolComportamiento()
        self.camino = []

        # Dibujo el enemigo con un color rojo simple
        self.image = pygame.Surface((tile_size - 4, tile_size - 4), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (220, 50, 50), (0, 0, tile_size - 4, tile_size - 4), border_radius=6)
        pygame.draw.circle(self.image, (255, 220, 180), ((tile_size - 4) // 2, (tile_size - 4) // 4), (tile_size - 4) // 4)

    def update(self, dt, jugador, mapa, bombas):
        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            # Ejecuto el árbol de comportamiento
            self.arbol.ejecutar(self, jugador, mapa, bombas)

    def perseguir(self, jugador, mapa):
        # Uso A* para encontrar el camino al jugador
        inicio = (self.row, self.col)
        fin = (jugador.y // self.tile_size, jugador.x // self.tile_size)
        astar = AStar(mapa)
        self.camino = astar.buscar(inicio, fin)

        # Me muevo al siguiente tile del camino
        if self.camino:
            siguiente = self.camino[0]
            self.row = siguiente[0]
            self.col = siguiente[1]
            self.x = self.col * self.tile_size
            self.y = self.row * self.tile_size

    def huir_de_bomba(self, bomba, mapa):
        # Me muevo en dirección opuesta a la bomba
        direcciones = [(0,1),(0,-1),(1,0),(-1,0)]
        random.shuffle(direcciones)
        for dr, dc in direcciones:
            nuevo_row = self.row + dr
            nuevo_col = self.col + dc
            if not mapa.es_pared(nuevo_row, nuevo_col):
                dist_actual = abs(self.row - bomba.row) + abs(self.col - bomba.col)
                dist_nueva = abs(nuevo_row - bomba.row) + abs(nuevo_col - bomba.col)
                if dist_nueva > dist_actual:
                    self.row = nuevo_row
                    self.col = nuevo_col
                    self.x = self.col * self.tile_size
                    self.y = self.row * self.tile_size
                    return

    def patrullar(self, mapa):
        # Me muevo en una dirección aleatoria libre
        direcciones = [(0,1),(0,-1),(1,0),(-1,0)]
        random.shuffle(direcciones)
        for dr, dc in direcciones:
            nuevo_row = self.row + dr
            nuevo_col = self.col + dc
            if not mapa.es_pared(nuevo_row, nuevo_col):
                self.row = nuevo_row
                self.col = nuevo_col
                self.x = self.col * self.tile_size
                self.y = self.row * self.tile_size
                return

    def draw(self, screen):
        screen.blit(self.image, (self.x + 2, self.y + 2))