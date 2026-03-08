# Johanna Foston 22-SISN-2-036
import pygame
from scripts.player import Player
from scripts.map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bomberman IA")
        self.clock = pygame.time.Clock()
        self.running = True
        self.tile_size = 40
        

        self.map = Map(self.tile_size)
        self.player = Player(45, 45, 36)

    def run(self):
        while self.running:
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Movimiento del jugador
            keys = pygame.key.get_pressed()
            self.player.move(keys, 800, 600, self.map, self.tile_size)

            # Dibujar fondo
            self.screen.fill((30, 30, 30))
            self.map.draw(self.screen)

            # Dibujar jugador (Una sola vez, fuera del grid)
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)  # Solo una vez

        pygame.quit()