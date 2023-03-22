import random

import pygame


class Pong:
    def __init__(self):
        self.largura_tela = 1000
        self.altura_tela = 700
        self.largura_jogo = 600
        self.altura_jogo = self.altura_tela

        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Pong!")
        self.fonte = pygame.font.SysFont("Arial", 40)
        self.background = pygame.image.load('imagem/background.jpeg')
        self.background = pygame.transform.scale(self.background, (self.largura_jogo, self.altura_jogo))

        self.pontuacao_maxima = 5
        self.placar_jogador = 0
        self.placar_robo = 0

        self.jogando = False

    def reiniciar(self, bola, robo, jogadores):
        bola.corpo.center = [int(self.largura_jogo / 2), int(self.altura_jogo / 2)]
        robo.corpo.center = [int(self.largura_jogo / 2), 20]

        bola.velocidade_x = 5 * random.choice((-1, 1))
        bola.velocidade_y = 5 * random.choice((-1, 1))

        todos_mortos = True
        for jogador in jogadores:
            jogador.corpo.center = [int(self.largura_jogo / 2), int(self.altura_jogo - 20)]
            if jogador.vivo:
                todos_mortos = False

        if todos_mortos:
            for jogador in jogadores:
                jogador.vivo = True

    def reiniciar_partida(self, bola, robo, jogadores):
        self.placar_robo = 0
        self.placar_jogador = 0

        for jogador in jogadores:
            jogador.fitness = 0

        self.reiniciar(bola, robo, jogadores)

    def atualiza_frame(self, bola, robo, jogadores):
        bola.move()

        # colisao bola nas paredes
        if bola.corpo.right >= self.largura_jogo:
            bola.velocidade_x *= -1
        elif bola.corpo.left <= 0:
            bola.velocidade_x *= -1

        # colisao bola fundo da quadra
        if bola.corpo.top <= 0:
            self.placar_jogador += 1
            for jogador in jogadores:
                if jogador.vivo:
                    jogador.fitness += 1
            self.reiniciar(bola, robo, jogadores)
        elif bola.corpo.bottom >= self.altura_jogo:
            self.placar_robo += 1
            self.reiniciar(bola, robo, jogadores)

        # movimeta robo para seguir a bola
        if robo.corpo.left > bola.corpo.right:
            robo.move_esquerda(0)
        elif robo.corpo.right < bola.corpo.left:
            robo.move_direita(self.largura_jogo)

        # colisao bola e robo
        if bola.corpo.top >= 20:
            if bola.corpo.colliderect(robo.corpo):
                bola.velocidade_y *= -1
                bola.velocidade_x = bola.velocidade_x + random.randint(-1, 1)

        # verificar colisao dos jogadores com a bola
        bola_colidiu = False
        if bola.corpo.bottom >= self.altura_jogo - 20:
            for jogador in jogadores:
                if jogador.vivo:
                    if not jogador.corpo.colliderect(bola.corpo):
                        jogador.vivo = False
                    else:
                        bola_colidiu = True
                        jogador.fitness += 0.1

        if bola_colidiu:
            bola.velocidade_y *= -1
            bola.velocidade_x = bola.velocidade_x + random.randint(-1, 1)

        if self.placar_robo >= self.pontuacao_maxima:
            return True
        return False
