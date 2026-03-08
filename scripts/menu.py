# Johanna Foston 22-SISN-2-036
import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.fuente_titulo = pygame.font.SysFont("Arial", 60, bold=True)
        self.fuente_opciones = pygame.font.SysFont("Arial", 35)
        self.fuente_pequeña = pygame.font.SysFont("Arial", 25)

        # Aquí defino los colores que uso en el menú
        self.color_fondo = (20, 20, 20)
        self.color_titulo = (255, 150, 0)
        self.color_opcion = (255, 255, 255)
        self.color_seleccion = (255, 150, 0)

        self.opciones = ["Iniciar juego", "Salir"]
        self.seleccion = 0

    def dibujar(self):
        self.screen.fill(self.color_fondo)

        # Dibujo el título
        titulo = self.fuente_titulo.render("BOMBERMAN IA", True, self.color_titulo)
        self.screen.blit(titulo, (400 - titulo.get_width() // 2, 150))

        # Dibujo las opciones
        for i, opcion in enumerate(self.opciones):
            color = self.color_seleccion if i == self.seleccion else self.color_opcion
            texto = self.fuente_opciones.render(opcion, True, color)
            self.screen.blit(texto, (400 - texto.get_width() // 2, 300 + i * 60))

        # Dibujo instrucciones abajo
        instruccion = self.fuente_pequeña.render("Usa las flechas y Enter para seleccionar", True, (150, 150, 150))
        self.screen.blit(instruccion, (400 - instruccion.get_width() // 2, 520))

        pygame.display.flip()

    def manejar_eventos(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Muevo la selección hacia arriba
                self.seleccion = (self.seleccion - 1) % len(self.opciones)
            if event.key == pygame.K_DOWN:
                # Muevo la selección hacia abajo
                self.seleccion = (self.seleccion + 1) % len(self.opciones)
            if event.key == pygame.K_RETURN:
                # Devuelvo la opción seleccionada
                return self.opciones[self.seleccion]
        return None

class MenuGameOver:
    def __init__(self, screen):
        self.screen = screen
        self.fuente_titulo = pygame.font.SysFont("Arial", 60, bold=True)
        self.fuente_opciones = pygame.font.SysFont("Arial", 35)

        self.opciones = ["Reiniciar", "Salir"]
        self.seleccion = 0
        self.color_seleccion = (255, 150, 0)
        self.color_opcion = (255, 255, 255)

    def dibujar(self, gano):
        self.screen.fill((20, 20, 20))

        # Muestro si ganó o perdió
        if gano:
            texto = self.fuente_titulo.render("¡GANASTE! 🎉", True, (0, 255, 100))
        else:
            texto = self.fuente_titulo.render("¡PERDISTE! 💀", True, (255, 50, 50))
        self.screen.blit(texto, (400 - texto.get_width() // 2, 150))

        # Dibujo las opciones
        for i, opcion in enumerate(self.opciones):
            color = self.color_seleccion if i == self.seleccion else self.color_opcion
            t = self.fuente_opciones.render(opcion, True, color)
            self.screen.blit(t, (400 - t.get_width() // 2, 320 + i * 60))

        pygame.display.flip()

    def manejar_eventos(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.seleccion = (self.seleccion - 1) % len(self.opciones)
            if event.key == pygame.K_DOWN:
                self.seleccion = (self.seleccion + 1) % len(self.opciones)
            if event.key == pygame.K_RETURN:
                return self.opciones[self.seleccion]
        return None