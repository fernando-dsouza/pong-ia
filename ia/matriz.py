import numpy as np


class Matriz:
    def __init__(self, linhas=0, colunas=0):
        self.linhas = linhas
        self.colunas = colunas
        self.data = np.zeros([linhas, colunas]).tolist()

    def randomizar(self, minimo, maximo):
        matriz = np.random.rand(self.linhas, self.colunas)
        matriz = matriz * (maximo - minimo) + minimo
        self.data = matriz

    @staticmethod
    def map(matriz_a, function):
        matriz = Matriz(matriz_a.linhas, matriz_a.colunas)
        matriz.data = list(map(lambda x: list(map(lambda i: function(i), x)), matriz_a.data))
        return matriz

    @staticmethod
    def lista_para_matriz(array):
        matriz = Matriz(1, len(array))
        data = []
        for i in array:
            data.append([i])
        matriz.data = data
        return matriz

    @staticmethod
    def matriz_para_lista(matriz_a):
        array = []
        for data in matriz_a.data:
            array.append(data)
        return array

    @staticmethod
    def soma(matriz_a, matriz_b):
        matriz = Matriz(matriz_a.linhas, matriz_b.colunas)
        matriz.data = np.add(matriz_a.data, matriz_b.data).tolist()
        return matriz

    @staticmethod
    def multiplica(matriz_a, matriz_b):
        matriz = Matriz(matriz_a.linhas, matriz_b.colunas)
        matriz.data = np.dot(matriz_a.data, matriz_b.data).tolist()
        return matriz
