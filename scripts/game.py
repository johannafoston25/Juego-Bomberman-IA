# Johanna Foston 22-SISN-2-036
import pygame
from scripts.player import Player
from scripts.map import Map
from scripts.bomb import Bomb
from scripts.enemy import Enemy
from scripts.menu import Menu, MenuGameOver

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bomberman IA")
        self.clock = pygame.time.Clock()
        self.running = True

        # Aquí defino los estados del juego
        self.estado = "menu"  # puede ser: menu, jugando, gameover
        self.gano = False
        self.tile_size = 40

        self.menu = Menu(self.screen)
        self.menu_gameover = MenuGameOver(self.screen)

        self.iniciar_juego()

    def iniciar_juego(self):
        # Aquí reinicio todos los elementos del juego
        self.map = Map(self.tile_size)
        self.player = Player(45, 45, 36)
        self.bombas = []
        self.enemy = Enemy(680, 480, self.tile_size)

    def verificar_colisiones(self):
        # Verifico si el enemigo tocó al jugador
        jugador_rect = pygame.Rect(self.player.x, self.player.y, self.player.size, self.player.size)
        enemigo_rect = pygame.Rect(self.enemy.x, self.enemy.y, self.tile_size - 4, self.tile_size - 4)

        if jugador_rect.colliderect(enemigo_rect):
            self.gano = False
            self.estado = "gameover"

        # Verifico si la explosión tocó al jugador o al enemigo
        for bomba in self.bombas:
            if bomba.mostrando_explosion:
                for (r, c) in bomba.get_tiles_explosion():
                    # Si la explosión toca al jugador pierde
                    jugador_row = self.player.y // self.tile_size
                    jugador_col = self.player.x // self.tile_size
                    if r == jugador_row and c == jugador_col:
                        self.gano = False
                        self.estado = "gameover"

                    # Si la explosión toca al enemigo gana
                    if r == self.enemy.row and c == self.enemy.col:
                        self.gano = True
                        self.estado = "gameover"

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if self.estado == "menu":
                    resultado = self.menu.manejar_eventos(event)
                    if resultado == "Iniciar juego":
                        self.iniciar_juego()
                        self.estado = "jugando"
                    elif resultado == "Salir":
                        self.running = False

                elif self.estado == "gameover":
                    resultado = self.menu_gameover.manejar_eventos(event)
                    if resultado == "Reiniciar":
                        self.iniciar_juego()
                        self.estado = "jugando"
                    elif resultado == "Salir":
                        self.running = False

                elif self.estado == "jugando":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # Coloco una bomba donde está el jugador
                            bomba = Bomb(self.player.x, self.player.y, self.tile_size)
                            self.bombas.append(bomba)

            if self.estado == "menu":
                self.menu.dibujar()

            elif self.estado == "gameover":
                self.menu_gameover.dibujar(self.gano)

            elif self.estado == "jugando":
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

                # Verifico si alguien ganó o perdió
                self.verificar_colisiones()

                # Dibujar todo
                self.screen.fill((30, 30, 30))
                self.map.draw(self.screen)

                for bomba in self.bombas:
                    bomba.draw(self.screen)

                self.enemy.draw(self.screen)
                self.player.draw(self.screen)

                pygame.display.flip()
                self.clock.tick(60)

        pygame.quit()