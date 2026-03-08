# Johanna Foston 22-SISN-2-036
import pygame
from scripts.player import Player
from scripts.map import Map
from scripts.bomb import Bomb
from scripts.enemy import Enemy

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

        # Aquí creo el enemigo en la esquina opuesta al jugador
        self.enemy = Enemy(680, 480, self.tile_size)

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

            # Actualizo el enemigo
            self.enemy.update(dt, self.player, self.map, self.bombas)

            # Dibujar fondo
            self.screen.fill((30, 30, 30))
            self.map.draw(self.screen)

            # Dibujo todas las bombas
            for bomba in self.bombas:
                bomba.draw(self.screen)

            # Dibujo el enemigo
            self.enemy.draw(self.screen)

            # Dibujar jugador
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()