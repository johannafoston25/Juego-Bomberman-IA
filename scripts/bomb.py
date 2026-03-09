# Johanna Foston 22-SISN-2-036
import pygame

class Bomb:
    def __init__(self, x, y, tile_size):
        # Posición en el grid
        self.col = x // tile_size
        self.row = y // tile_size
        self.tile_size = tile_size

        # Posición en píxeles (centrada en el tile)
        self.x = self.col * tile_size
        self.y = self.row * tile_size

        self.timer = 1000        # explota en 1 segundos
        self.explotada = False
        self.radio = 2           # cuántos tiles alcanza la explosión
        self.explosion_timer = 500  # la explosión dura 0.5 segundos
        self.mostrando_explosion = False

    def update(self, dt, mapa):
        if not self.explotada:
            self.timer -= dt
            if self.timer <= 0:
                self.explotar(mapa)
        else:
            # Aqui Cuenta el tiempo de la explosión
            self.explosion_timer -= dt
            if self.explosion_timer <= 0:
                self.mostrando_explosion = False

    def explotar(self, mapa):
        self.explotada = True
        self.mostrando_explosion = True

        # Aquí destruyo los bloques en 4 direcciones
        direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in direcciones:
            for i in range(1, self.radio + 1):
                r = self.row + dr * i
                c = self.col + dc * i
                if mapa.es_pared(r, c):
                    mapa.destruir_bloque(r, c)
                    break  # la explosión se detiene en paredes

    def get_tiles_explosion(self):
        # Devuelve los tiles que cubre la explosión
        tiles = [(self.row, self.col)]
        direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in direcciones:
            for i in range(1, self.radio + 1):
                tiles.append((self.row + dr * i, self.col + dc * i))
        return tiles

    def draw(self, screen):
        if not self.explotada:
            # Aquí dibujo la bomba en pantalla
            cx = self.x + self.tile_size // 2
            cy = self.y + self.tile_size // 2
            pygame.draw.circle(screen, (20, 20, 20), (cx, cy), self.tile_size // 3)
            pygame.draw.circle(screen, (255, 100, 0), (cx - 4, cy - 10), 5)  # mecha
        elif self.mostrando_explosion:
            # Aqui dibujo la explosion
            for (r, c) in self.get_tiles_explosion():
                rect = pygame.Rect(
                    c * self.tile_size,
                    r * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
                pygame.draw.rect(screen, (255, 150, 0), rect)