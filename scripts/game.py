# Johanna Foston 22-SISN-2-036
import pygame
from scripts.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bomberman IA")
        self.clock = pygame.time.Clock()
        self.running = True
        self.tile_size = 40
        self.rows = 15
        self.cols = 20

        self.player = Player(100, 100, 36)

    def run(self):
        while self.running:
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Movimiento del jugador
            keys = pygame.key.get_pressed()
            self.player.move(keys, 800, 600)

            # Dibujar fondo
            self.screen.fill((30, 30, 30))

            # Dibujar grid
            for row in range(self.rows):
                for col in range(self.cols):
                    rect = pygame.Rect(
                        col * self.tile_size,
                        row * self.tile_size,
                        self.tile_size,
                        self.tile_size
                    )
                    pygame.draw.rect(self.screen, (60, 60, 60), rect, 1)

            # Dibujar jugador (Una sola vez, fuera del grid)
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)  # Solo una vez

        pygame.quit()