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

    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Evita que el jugador se salga de la pantalla
        self.x = max(0, min(self.x, screen_width - self.size))
        self.y = max(0, min(self.y, screen_height - self.size))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))