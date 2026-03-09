# Johanna Foston 22-SISN-2-036
import pygame

# 0 = piso, 1 = pared fija, 2 = bloque destructible
MAPA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.mapa = [fila[:] for fila in MAPA]  # copia del mapa original

        # Colores de cada tile
        self.colores = {
           0: (34, 139, 34),    # piso verde
           1: (40, 40, 40),     # pared fija
           2: (160, 100, 50),   # bloque destructible
        }

    def draw(self, screen):
        for row in range(len(self.mapa)):
            for col in range(len(self.mapa[row])):
                tile = self.mapa[row][col]
                color = self.colores[tile]
                rect = pygame.Rect(
                    col * self.tile_size,
                    row * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
                pygame.draw.rect(screen, color, rect)
                # Borde para que se vean los tiles
                pygame.draw.rect(screen, (20, 20, 20), rect, 1)

    def es_pared(self, row, col):
        # Devuelve True si el tile es una pared (no se puede pasar)
        if row < 0 or col < 0 or row >= len(self.mapa) or col >= len(self.mapa[0]):
            return True
        return self.mapa[row][col] != 0

    def destruir_bloque(self, row, col):
        # Destruye un bloque si es destructible
        if self.mapa[row][col] == 2:
            self.mapa[row][col] = 0