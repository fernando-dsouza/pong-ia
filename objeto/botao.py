import pygame


class Botao:
    def __init__(self, screen, x, y, width, height, text, cor):
        self.rect = pygame.Rect(x, y, width, height)
        self.cor = cor
        self.text = text
        self.cor_texto = (255, 255, 255)
        self.screen = screen

    def desenha(self):
        pygame.draw.rect(self.screen, self.cor, self.rect, border_radius=12)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, self.cor_texto)
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)
