# Johanna Foston 22-SISN-2-036
import pygame

class Sonidos:
    def __init__(self):
        pygame.mixer.init()

        # Aquí cargo todos los sonidos del juego
        self.explosion = pygame.mixer.Sound("assets/sounds/explosion.wav")
        self.bomba = pygame.mixer.Sound("assets/sounds/bomb.wav")
        self.gameover = pygame.mixer.Sound("assets/sounds/game-over.wav")

        # Aquí ajusto el volumen de los sonidos
        self.explosion.set_volume(0.7)
        self.bomba.set_volume(0.5)
        self.gameover.set_volume(0.8)

    def reproducir_explosion(self):
        self.explosion.play()

    def reproducir_bomba(self):
        self.bomba.play()

    def reproducir_gameover(self):
        self.gameover.play()

    def iniciar_musica(self):
        # Aquí inicio la música de fondo en loop
        pygame.mixer.music.load("assets/music/musica.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)  # -1 significa que se repite forever

    def detener_musica(self):
        pygame.mixer.music.stop()