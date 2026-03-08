# Johanna Foston 22-SISN-2-036
import pygame
from scripts.player import Player
from scripts.map import Map
from scripts.bomb import Bomb

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
        self.bombas = []  # aquí guardo todas las bombas activas

    def run(self):
        while self.running:
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Coloco una bomba donde está el jugador
                        bomba = Bomb(self.player.x, self.player.y, self.tile_size)
                        self.bombas.append(bomba)

            # Movimiento del jugador
            keys = pygame.key.get_pressed()
            self.player.move(keys, 800, 600, self.map, self.tile_size)

            # Actualizo y limpio las bombas que ya terminaron
            dt = self.clock.get_time()
            self.bombas = [b for b in self.bombas if b.explosion_timer > 0 or not b.explotada]
            for bomba in self.bombas:
                bomba.update(dt, self.map)

            # Dibujar fondo
            self.screen.fill((30, 30, 30))
            self.map.draw(self.screen)

            # Dibujo todas las bombas
            for bomba in self.bombas:
                bomba.draw(self.screen)

            # Dibujar jugador (Una sola vez, fuera del grid)
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)  # Solo una vez

        pygame.quit()