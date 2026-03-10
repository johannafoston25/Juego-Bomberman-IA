# Johanna Foston 22-SISN-2-036
import pygame
from scripts.game import Game

# Aqui inicio el juego
def main():
    pygame.init()
    game = Game() # Aqui creo la instacia del juego
    game.run()    # Aqui arranco el loop principal


if __name__ == "__main__":
    main()