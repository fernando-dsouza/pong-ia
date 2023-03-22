import pygame


class Jogador:
    def __init__(self, x, y, width, height, cor):
        self.corpo = pygame.Rect(x, y, width, height)
        self.cor = cor
        self.velocidade = 5
        self.nn = None
        self.fitness = 0
        self.vivo = True

    def move_esquerda(self, limite):
        if self.corpo.left <= limite:
            self.corpo.left = limite
        else:
            self.corpo.x -= self.velocidade

    def move_direita(self, limite):
        if self.corpo.right >= limite:
            self.corpo.right = limite
        else:
            self.corpo.right += self.velocidade
