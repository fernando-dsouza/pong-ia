from ia.matriz import Matriz

import numpy as np


class RedeNeural:
    def __init__(self, n_entradas, n_ocultos, n_saidas):
        self.n_entradas = n_entradas
        self.n_ocultos = n_ocultos
        self.n_saidas = n_saidas

        self.bias_eo = Matriz(self.n_ocultos, 1)
        self.bias_eo.randomizar(-1, 1)
        self.bias_os = Matriz(self.n_saidas, 1)
        self.bias_os.randomizar(-1, 1)

        self.pesos_eo = Matriz(self.n_ocultos, self.n_entradas)
        self.pesos_eo.randomizar(-1, 1)
        self.pesos_os = Matriz(self.n_saidas, self.n_ocultos)
        self.pesos_os.randomizar(-1, 1)

        self.fitness = 0

    def carrega_neuronios(self, lista):
        itens = ((self.pesos_eo.linhas * self.pesos_eo.colunas) +
                 (self.pesos_os.linhas * self.pesos_os.colunas) +
                 (self.bias_eo.linhas * self.bias_eo.colunas) +
                 (self.bias_os.linhas * self.bias_os.colunas))

        if itens != len(lista):
            raise Exception(f'Erro ao carregar rede: Pesos da rede {itens}, pesos informados {len(lista)}')

        pesos_eo = Matriz.matriz_para_lista(self.pesos_eo)
        bias_eo = Matriz.matriz_para_lista(self.bias_eo)
        pesos_os = Matriz.matriz_para_lista(self.pesos_os)
        bias_os = Matriz.matriz_para_lista(self.bias_os)

        cont = 0
        for index_r, linhas in enumerate(pesos_eo):
            for index_c, colunas in enumerate(linhas):
                pesos_eo[index_r][index_c] = lista[cont]
                cont += 1

        for index_r, linhas in enumerate(bias_eo):
            for index_c, colunas in enumerate(linhas):
                bias_eo[index_r][index_c] = lista[cont]
                cont += 1

        for index_r, linhas in enumerate(pesos_os):
            for index_c, colunas in enumerate(linhas):
                pesos_os[index_r][index_c] = lista[cont]
                cont += 1

        for index_r, linhas in enumerate(bias_os):
            for index_c, colunas in enumerate(linhas):
                bias_os[index_r][index_c] = lista[cont]

        self.pesos_eo.data = pesos_eo
        self.bias_eo.data = bias_eo
        self.pesos_os.data = pesos_os
        self.bias_os.data = bias_os

    def busca_neuronios(self):
        rede = []
        for linha in Matriz.matriz_para_lista(self.pesos_eo):
            for coluna in linha:
                rede.append(coluna)
        for linha in Matriz.matriz_para_lista(self.bias_eo):
            for coluna in linha:
                rede.append(coluna)
        for linha in Matriz.matriz_para_lista(self.pesos_os):
            for coluna in linha:
                rede.append(coluna)
        for linha in Matriz.matriz_para_lista(self.bias_os):
            for coluna in linha:
                rede.append(coluna)
        return rede

    @staticmethod
    def relu(x):
        if x > 0:
            return x
        else:
            return 0

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def previsao(self, array):
        entradas = Matriz.lista_para_matriz(array)

        oculta = Matriz.multiplica(self.pesos_eo, entradas)
        oculta = Matriz.soma(oculta, self.bias_eo)
        oculta = Matriz.map(oculta, self.relu)

        # HIDDEN -> OUTPUT
        saida = Matriz.multiplica(self.pesos_os, oculta)
        saida = Matriz.soma(saida, self.bias_os)
        saida = Matriz.map(saida, self.relu)
        saida = Matriz.matriz_para_lista(saida)

        saida = self.softmax(np.array([saida[0][0], saida[1][0]]))
        return saida, oculta.data
