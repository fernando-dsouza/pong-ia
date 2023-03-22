import time
import pygame
import sys
import random

from objeto.pong import Pong
from objeto import cor as Cor
from objeto.bola import Bola
from objeto.jogador import Jogador
from objeto.botao import Botao
from ia.rede_neural import RedeNeural
from objeto.dash import Dash
from ia.algoritmo_genetico import Genes


def gerar_populacao(n_individuos, rede_treinada=False, arquivo_rede_neural=''):
    if rede_treinada:
        with open(arquivo_rede_neural, "r") as file:
            lines = file.readlines()

        rede = []
        for line in lines:
            rede.append(float(line.strip()))

        populacao = []
        for i in range(n_individuos):
            populacao.append(rede)
        return populacao
    else:
        return gene.gera_populacao()


def gera_nova_populacao(populacao):
    novos = []
    for i in range(n_individuos):
        individuo = Jogador(0, 0, 80, 10, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        nn = RedeNeural(3, 10, 2)
        nn.carrega_neuronios(populacao[i])
        individuo.nn = nn
        individuo.corpo.center = [int(pong.largura_jogo / 2), int(pong.altura_jogo - 20)]
        novos.append(individuo)
    return novos


def desenha_tela():
    pong.tela.fill(Cor.AZUL_QUADRA)
    pong.tela.blit(pong.background, (0, 0))

    pygame.draw.rect(pong.tela, bola.cor, bola.corpo, border_radius=10)
    pygame.draw.rect(pong.tela, Cor.PRETO, bola.corpo, border_radius=10, width=1)

    pygame.draw.rect(pong.tela, robo.cor, robo.corpo, border_radius=12)
    pygame.draw.rect(pong.tela, Cor.PRETO, robo.corpo, border_radius=12, width=1)

    botao_start.desenha()
    botao_reset.desenha()
    botao_salvar.desenha()

    n_vivos = 0

    for jogador in jogadores:
        if jogador.vivo:
            n_vivos += 1
            pygame.draw.rect(pong.tela, jogador.cor, jogador.corpo, border_radius=12)
            pygame.draw.rect(pong.tela, Cor.PRETO, jogador.corpo, border_radius=12, width=1)

    dash.placar(pong.placar_robo, pong.placar_jogador)
    dash.geracao(geracao)
    dash.vivos(n_vivos)
    dash.fps(TICK)
    dash.rede_neural(pong.tela)
    dash.texto_rede()
    dash.melhor_geracao(melhor_geracao, melhor_pontuacao)

    pygame.display.update()
    clock.tick(TICK)


if __name__ == '__main__':
    # inicial
    pygame.init()
    clock = pygame.time.Clock()

    # setup
    n_individuos = 20
    rede_treinada = False
    arquivo_rede = 'pesos_geracao_64.txt'

    # variaveis
    geracao = 1
    jogando = False
    melhor_geracao = 1
    melhor_pontuacao = 0
    TICK = 60  # FPS velocidade de atualização da tela

    # instancias
    pong = Pong()

    botao_start = Botao(pong.tela, 650, 630, 80, 35, 'Start', Cor.VERDE)
    botao_reset = Botao(pong.tela, 750, 630, 80, 35, 'Reset', Cor.AZUL)
    botao_salvar = Botao(pong.tela, 850, 630, 80, 35, 'Salvar', Cor.VERDE_QUADRA)

    dash = Dash(pong.tela)

    bola = Bola(0, 0, Cor.BRANCO)
    bola.corpo.center = [int(pong.largura_jogo / 2), int(pong.altura_jogo / 2)]

    robo = Jogador(0, 0, 80, 10, Cor.BRANCO)
    robo.corpo.center = [int(pong.largura_jogo / 2), 20]
    robo.velocidade = 5.5

    # populacao, genes e individuos
    gene = Genes(n_individuos, 62, -1, 1)
    populacao = gerar_populacao(n_individuos, rede_treinada=rede_treinada, arquivo_rede_neural=arquivo_rede)
    jogadores = gera_nova_populacao(populacao)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se as coordenadas do clique do mouse estão dentro do objeto Rect
                if botao_start.rect.collidepoint(event.pos):
                    botao_start.cor = Cor.CINZA
                    botao_start.desenha()
                    pygame.display.update()
                    time.sleep(0.1)
                    jogando = not jogando
                    if jogando:
                        botao_start.cor = Cor.VERMELHO
                        botao_start.text = 'Stop'
                    else:
                        botao_start.cor = Cor.VERDE
                        botao_start.text = 'Start'
                if botao_reset.rect.collidepoint(event.pos):
                    botao_reset.cor = Cor.CINZA
                    botao_reset.desenha()
                    pygame.display.update()
                    time.sleep(0.1)
                    pong.reiniciar_partida(bola, robo, jogadores)
                    populacao = gerar_populacao(n_individuos, rede_treinada=False)
                    jogadores = gera_nova_populacao(populacao)
                    geracao = 1
                    botao_reset.cor = Cor.AZUL
                if botao_start.text == 'Stop':
                    botao_salvar.cor = Cor.CINZA
                else:
                    botao_salvar.cor = Cor.VERDE_QUADRA
                    if botao_salvar.rect.collidepoint(event.pos):
                        melhor = sorted(jogadores, key=lambda x: x.fitness, reverse=True)

                        print('Salvando rede neural')
                        network = melhor[0].nn.busca_neuronios()
                        with open(f'pesos_geracao_{geracao}.txt', "w") as file:
                            for item in network:
                                file.write("%s\n" % item)

        keys = pygame.key.get_pressed()
        # velocidade do jogo - FPS
        if keys[pygame.K_UP]:
            TICK += 1
        elif keys[pygame.K_DOWN]:
            TICK -= 1

        # controle manual
        if keys[pygame.K_LEFT]:
            jogadores[0].move_esquerda(0)
        elif keys[pygame.K_RIGHT]:
            jogadores[0].move_direita(pong.largura_jogo)

        if jogando:
            for jogador in jogadores:
                if jogador.vivo:
                    previsao, ocultos = jogador.nn.previsao(
                        [bola.corpo.x - jogador.corpo.x, bola.corpo.y, jogador.corpo.x])

                    if previsao[0] >= 0.7:
                        jogador.move_esquerda(0)
                        dash.saida1 = 1
                    else:
                        dash.saida1 = 0

                    if previsao[1] >= 0.7:
                        jogador.move_direita(pong.largura_jogo)
                        dash.saida2 = 1
                    else:
                        dash.saida2 = 0

                    dash.entrada1 = bola.corpo.x - jogador.corpo.x
                    dash.entrada2 = bola.corpo.y
                    dash.entrada3 = jogador.corpo.x
                    dash.oculta1 = ocultos[0][0]
                    dash.oculta2 = ocultos[1][0]
                    dash.oculta3 = ocultos[2][0]
                    dash.oculta4 = ocultos[3][0]
                    dash.oculta5 = ocultos[4][0]
                    dash.oculta6 = ocultos[5][0]
                    dash.oculta7 = ocultos[6][0]
                    dash.oculta8 = ocultos[7][0]
                    dash.oculta9 = ocultos[8][0]
                    dash.oculta10 = ocultos[9][0]

        if jogando:
            fim_partida = pong.atualiza_frame(bola, robo, jogadores)

            if fim_partida:
                if pong.placar_jogador > melhor_pontuacao:
                    melhor_pontuacao = pong.placar_jogador
                    melhor_geracao = geracao

                # escolher os dois melhores
                melhores = sorted(jogadores, key=lambda x: x.fitness, reverse=True)
                nova_populacao = gene.crossover(melhores[0].nn.busca_neuronios(), melhores[1].nn.busca_neuronios())
                nova_populacao = gene.mutacao(nova_populacao, taxa_mutacao=0.1)
                for i, jogador in enumerate(jogadores):
                    jogador.nn.carrega_neuronios(nova_populacao[i])
                geracao += 1
                pong.reiniciar_partida(bola, robo, jogadores)

        desenha_tela()
