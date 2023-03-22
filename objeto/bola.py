import pygame
import random


class Bola:
    def __init__(self, x, y, cor):
        self.corpo = pygame.Rect(x, y, 20, 20)
        self.cor = cor
        self.cor_texto = (0, 0, 0)
        self.velocidade_x = 5 * random.choice((-1, 1))
        self.velocidade_y = 5 * random.choice((-1, 1))

    def move(self):
        self.corpo.x += self.velocidade_x
        self.corpo.y += self.velocidade_y
