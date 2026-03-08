# Johanna Foston 22-SISN-2-036
import pygame
from scripts.player import Player
from scripts.map import Map
from scripts.bomb import Bomb
from scripts.enemy import Enemy
from scripts.menu import Menu, MenuGameOver
from scripts.sonidos import Sonidos

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Bomberman IA")
        self.clock = pygame.time.Clock()
        self.running = True

        # Aquí defino los estados del juego
        self.estado = "menu"
        self.gano = False
        self.ancho = self.screen.get_width()
        self.alto = self.screen.get_height()

       # Aquí calculo el tile_size para que el mapa llene toda la pantalla
        self.tile_size = max(self.ancho // 20, self.alto // 15)

        self.menu = Menu(self.screen)
        self.menu_gameover = MenuGameOver(self.screen)
        self.sonidos = Sonidos()

        # Aquí inicio la música de fondo
        self.sonidos.iniciar_musica()

        self.iniciar_juego()

    def iniciar_juego(self):
        # Aquí reinicio todos los elementos del juego
        self.map = Map(self.tile_size)
        self.player = Player(self.tile_size + 5, self.tile_size + 5, self.tile_size - 4)
        self.bombas = []
        self.enemy = Enemy(self.tile_size * 17, self.tile_size * 12, self.tile_size)

    def verificar_colisiones(self):
        # Verifico si el enemigo tocó al jugador
        jugador_rect = pygame.Rect(self.player.x, self.player.y, self.player.size, self.player.size)
        enemigo_rect = pygame.Rect(self.enemy.x, self.enemy.y, self.tile_size - 4, self.tile_size - 4)

        if jugador_rect.colliderect(enemigo_rect):
            self.gano = False
            self.sonidos.reproducir_gameover()
            self.estado = "gameover"

        # Verifico si la explosión tocó al jugador o al enemigo
        for bomba in self.bombas:
            if bomba.mostrando_explosion:
                for (r, c) in bomba.get_tiles_explosion():
                    jugador_row = self.player.y // self.tile_size
                    jugador_col = self.player.x // self.tile_size
                    if r == jugador_row and c == jugador_col:
                        self.gano = False
                        self.sonidos.reproducir_gameover()
                        self.estado = "gameover"

                    if r == self.enemy.row and c == self.enemy.col:
                        self.gano = True
                        self.sonidos.reproducir_gameover()
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
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                        if event.key == pygame.K_SPACE:
                            # Coloco una bomba y reproduzco el sonido
                            bomba = Bomb(self.player.x, self.player.y, self.tile_size)
                            self.bombas.append(bomba)
                            self.sonidos.reproducir_bomba()

            if self.estado == "menu":
                self.menu.dibujar()

            elif self.estado == "gameover":
                self.menu_gameover.dibujar(self.gano)

            elif self.estado == "jugando":
                keys = pygame.key.get_pressed()
                self.player.move(keys, self.ancho, self.alto, self.map, self.tile_size)

                dt = self.clock.get_time()
                bombas_antes = len(self.bombas)
                self.bombas = [b for b in self.bombas if b.explosion_timer > 0 or not b.explotada]
                bombas_despues = len(self.bombas)

                for bomba in self.bombas:
                    explotada_antes = bomba.explotada
                    bomba.update(dt, self.map)
                    # Reproduzco sonido cuando explota
                    if not explotada_antes and bomba.explotada:
                        self.sonidos.reproducir_explosion()

                self.enemy.update(dt, self.player, self.map, self.bombas)
                self.verificar_colisiones()

                self.screen.fill((30, 30, 30))
                self.map.draw(self.screen)

                for bomba in self.bombas:
                    bomba.draw(self.screen)

                self.enemy.draw(self.screen)
                self.player.draw(self.screen)

                pygame.display.flip()
                self.clock.tick(60)

        pygame.quit()