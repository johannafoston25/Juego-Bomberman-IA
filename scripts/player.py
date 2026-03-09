# Johanna Foston 22-SISN-2-036
import pygame

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 4
        self.vidas = 3 #Aqui defino las vidas del jugador

        # Aquí cargo la imagen del jugador
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))

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

        # Verificamos si alguna esquina choca con pared
        puede_mover_x = True
        puede_mover_y = True

        esquinas_x = [
            (nueva_x, self.y),
            (nueva_x + self.size - 1, self.y),
            (nueva_x, self.y + self.size - 1),
            (nueva_x + self.size - 1, self.y + self.size - 1)
        ]
        esquinas_y = [
            (self.x, nueva_y),
            (self.x + self.size - 1, nueva_y),
            (self.x, nueva_y + self.size - 1),
            (self.x + self.size - 1, nueva_y + self.size - 1)
        ]

        for (ex, ey) in esquinas_x:
            col = int(ex // tile_size)
            row = int(ey // tile_size)
            if mapa.es_pared(row, col):
                puede_mover_x = False

        for (ex, ey) in esquinas_y:
            col = int(ex // tile_size)
            row = int(ey // tile_size)
            if mapa.es_pared(row, col):
                puede_mover_y = False

        if puede_mover_x:
            self.x = nueva_x
        if puede_mover_y:
            self.y = nueva_y

        # Aqui evita salirse de la pantalla
        self.x = max(0, min(self.x, screen_width - self.size))
        self.y = max(0, min(self.y, screen_height - self.size))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))