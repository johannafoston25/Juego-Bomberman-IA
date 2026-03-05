import pygame

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bomberman IA")
        self.clock = pygame.time.Clock()
        self.running = True
        self.tile_size = 40
        self.rows = self.height // self.tile_size
        self.cols = self.width // self.tile_size

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((30, 30, 30))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()