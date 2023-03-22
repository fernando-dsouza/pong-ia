import pygame


class Dash:
    def __init__(self, tela):
        self.tela = tela

        self.entrada1 = 0
        self.entrada2 = 0
        self.entrada3 = 0

        self.oculta1 = 0
        self.oculta2 = 0
        self.oculta3 = 0
        self.oculta4 = 0
        self.oculta5 = 0
        self.oculta6 = 0
        self.oculta7 = 0
        self.oculta8 = 0
        self.oculta9 = 0
        self.oculta10 = 0

        self.saida1 = 0
        self.saida2 = 0



    def placar(self, a, b, cor=(255, 255, 255)):
        font = pygame.font.SysFont("Arial", 30)
        texto = font.render(f'Bot {a} x {b} IA', True, cor)
        texto_rect = texto.get_rect()
        texto_rect.x = 630
        texto_rect.y = 35
        self.tela.blit(texto, texto_rect)

    def geracao(self, n_geracao, cor=(255, 255, 255)):
        font = pygame.font.SysFont("Arial", 25)
        texto = font.render(f'Geracao: {n_geracao}', True, cor)
        texto_rect = texto.get_rect()
        texto_rect.x = 630
        texto_rect.y = 85
        self.tela.blit(texto, texto_rect)

    def vivos(self, quantidade, cor=(255, 255, 255)):
        font = pygame.font.SysFont("Arial", 25)
        texto = font.render(f'Vivos: {quantidade}', True, cor)
        texto_rect = texto.get_rect()
        texto_rect.x = 630
        texto_rect.y = 125
        self.tela.blit(texto, texto_rect)

    def fps(self, tick, cor=(255, 255, 255)):
        font = pygame.font.SysFont("Arial", 25)
        texto = font.render(f'FPS: {tick}', True, cor)
        texto_rect = texto.get_rect()
        texto_rect.x = 630
        texto_rect.y = 165
        self.tela.blit(texto, texto_rect)

    def melhor_geracao(self, geracao, pontuacao, cor=(0, 0, 0)):
        font = pygame.font.SysFont("Arial", 16)
        texto = font.render(f'Melhor geração: {geracao} - Pontuacao: {pontuacao}', True, cor)
        texto_rect = texto.get_rect()
        texto_rect.x = 675
        texto_rect.y = 590
        self.tela.blit(texto, texto_rect)

    @staticmethod
    def peso(valor, minimo_entrada, maximo_entrada, minimo_saida, maximo_saida):
        if valor >= maximo_entrada:
            return maximo_saida
        if valor <= minimo_entrada:
            return minimo_saida
        return int((((valor - minimo_entrada) / (maximo_entrada - minimo_entrada)) * (
                maximo_saida - minimo_saida)) + minimo_saida)

    def rede_neural(self, tela):
        # ENTRADAS ##########################################
        # 1
        cor = self.peso(self.entrada1, -500, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (680, 350), 12)
        pygame.draw.circle(tela, (0, 0, 0), (680, 350), 12, 1)
        peso = self.peso(self.entrada1, -500, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 250), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 283), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 316), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 349), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 382), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 415), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 448), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 481), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 514), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 350), (780, 547), width=peso)
        # 2
        cor = self.peso(self.entrada2, 0, 700, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (680, 400), 12)
        pygame.draw.circle(tela, (0, 0, 0), (680, 400), 12, 1)
        peso = self.peso(self.entrada2, 0, 700, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 250), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 283), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 316), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 349), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 382), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 415), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 448), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 481), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 514), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 400), (780, 547), width=peso)
        # 3
        cor = self.peso(self.entrada3, 0, 600, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (680, 450), 12)
        pygame.draw.circle(tela, (0, 0, 0), (680, 450), 12, 1)
        peso = self.peso(self.entrada3, 0, 600, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 250), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 283), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 316), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 349), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 382), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 415), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 448), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 481), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 514), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (680, 450), (780, 547), width=peso)

        # OCULTOS ###########################################
        # 1
        cor = self.peso(self.oculta1, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 250), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 250), 12, 1)
        peso = self.peso(self.oculta1, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 250), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 250), (880, 430), width=peso)
        # 2
        cor = self.peso(self.oculta2, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 283), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 283), 12, 1)
        peso = self.peso(self.oculta2, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 283), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 283), (880, 430), width=peso)
        # 3
        cor = self.peso(self.oculta3, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 316), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 316), 12, 1)
        peso = self.peso(self.oculta3, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 316), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 316), (880, 430), width=peso)
        # 4
        cor = self.peso(self.oculta4, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 349), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 349), 12, 1)
        peso = self.peso(self.oculta4, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 349), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 349), (880, 430), width=peso)
        # 5
        cor = self.peso(self.oculta5, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 382), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 382), 12, 1)
        peso = self.peso(self.oculta5, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 382), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 382), (880, 430), width=peso)
        # 6
        cor = self.peso(self.oculta6, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 415), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 415), 12, 1)
        peso = self.peso(self.oculta6, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 415), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 415), (880, 430), width=peso)
        # 7
        cor = self.peso(self.oculta7, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 448), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 448), 12, 1)
        peso = self.peso(self.oculta7, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 448), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 448), (880, 430), width=peso)
        # 8
        cor = self.peso(self.oculta8, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 481), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 481), 12, 1)
        peso = self.peso(self.oculta8, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 481), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 481), (880, 430), width=peso)
        # 9
        cor = self.peso(self.oculta9, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 514), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 514), 12, 1)
        peso = self.peso(self.oculta9, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 514), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 514), (880, 430), width=peso)
        # 10
        cor = self.peso(self.oculta10, 0, 500, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (780, 547), 12)
        pygame.draw.circle(tela, (0, 0, 0), (780, 547), 12, 1)
        peso = self.peso(self.oculta10, 0, 500, 1, 6)
        pygame.draw.line(tela, (cor, 0, 0), (780, 547), (880, 367), width=peso)
        pygame.draw.line(tela, (cor, 0, 0), (780, 547), (880, 430), width=peso)

        # SAIDA #############################################
        # 1
        cor = self.peso(self.saida1, 0, 1, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (880, 367), 12)
        pygame.draw.circle(tela, (0, 0, 0), (880, 367), 12, 1)
        # 2
        cor = self.peso(self.saida2, 0, 1, 0, 200)
        pygame.draw.circle(tela, (cor, 0, 0), (880, 430), 12)
        pygame.draw.circle(tela, (0, 0, 0), (880, 430), 12, 1)

    def texto_rede(self):
        font = pygame.font.SysFont("Arial", 15)

        texto = font.render(f'Rede neural de uma das raquetes', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 670
        texto_rect.y = 210
        self.tela.blit(texto, texto_rect)

        texto = font.render(f'Sensores', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 620
        texto_rect.y = 300
        self.tela.blit(texto, texto_rect)

        texto = font.render(f'posicao', True, (0,0,0))
        texto_rect = texto.get_rect()
        texto_rect.x = 608
        texto_rect.y = 330
        self.tela.blit(texto, texto_rect)
        texto = font.render(f'bola', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 608
        texto_rect.y = 350
        self.tela.blit(texto, texto_rect)

        texto = font.render(f'altura', True, (0,0,0))
        texto_rect = texto.get_rect()
        texto_rect.x = 608
        texto_rect.y = 380
        self.tela.blit(texto, texto_rect)
        texto = font.render(f'bola', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 608
        texto_rect.y = 400
        self.tela.blit(texto, texto_rect)

        texto = font.render(f'posição', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 608
        texto_rect.y = 430
        self.tela.blit(texto, texto_rect)
        texto = font.render(f'jogador', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 608
        texto_rect.y = 450
        self.tela.blit(texto, texto_rect)

        texto = font.render(f'Ações', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 900
        texto_rect.y = 320
        self.tela.blit(texto, texto_rect)

        texto = font.render(f'Esquerda', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 900
        texto_rect.y = 358
        self.tela.blit(texto, texto_rect)

        texto = font.render(f'Direita', True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.x = 900
        texto_rect.y = 422
        self.tela.blit(texto, texto_rect)