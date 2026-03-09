# Johanna Foston 22-SISN-2-036
import pygame
from scripts.game import Game

# Aqui inicio el juego
def main():
    pygame.init()
    game = Game() # Aqui creo la instacia del juego
    game.run()    # Aqui arranco el loop principal

# Aquí verifico que el archivo se ejecute directamente y no como módulo
if __name__ == "__main__":
    main()