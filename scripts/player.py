# Johanna Foston 22-SISN-2-036
import pygame

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 4

        # Creamos un sprite simple con color hasta tener imagen
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 150, 255), (0, 0, size, size), border_radius=6)
        pygame.draw.circle(self.image, (255, 220, 180), (size // 2, size // 3), size // 4)  # cabeza

    def move(self, keys, screen_width, screen_height, mapa, tile_size):
        nueva_x = self.x
        nueva_y = self.y

        if keys[pygame.K_LEFT]:
            nueva_x -= self.speed
        if keys[pygame.K_RIGHT]:
            nueva_x += self.speed
        if keys[pygame.K_UP]:
            nueva_y -= self.speed
        if keys[pygame.K_DOWN]:
            nueva_y += self.speed

        # Revisamos las 4 esquinas del jugador para detectar colisión
        esquinas = [
            (nueva_x, nueva_y),
            (nueva_x + self.size - 1, nueva_y),
            (nueva_x, nueva_y + self.size - 1),
            (nueva_x + self.size - 1, nueva_y + self.size - 1)
        ]

        # Verificamos si alguna esquina choca con pared
        puede_mover_x = True
        puede_mover_y = True

        for (ex, ey) in esquinas:
            col = int(ex // tile_size)
            row = int(ey // tile_size)
            if mapa.es_pared(row, col):
                puede_mover_x = False
                puede_mover_y = False

        if puede_mover_x:
            self.x = nueva_x
        if puede_mover_y:
            self.y = nueva_y

        # Evita salirse de la pantalla
        self.x = max(0, min(self.x, screen_width - self.size))
        self.y = max(0, min(self.y, screen_height - self.size))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))