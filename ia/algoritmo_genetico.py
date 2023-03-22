import random


class Genes:
    def __init__(self, n_individos, n_cromossomos, menor_valor_crom=-1, maior_valor_crom=1):
        self.n_individos = n_individos
        self.n_cromossomos = n_cromossomos
        self.menor_valor_crom = menor_valor_crom
        self.maior_valor_crom = maior_valor_crom

    def gera_individos(self):
        individuo = []
        for i in range(self.n_cromossomos):
            individuo.append(random.uniform(self.menor_valor_crom, self.maior_valor_crom))
        return individuo

    def gera_populacao(self):
        populacao = []
        for i in range(self.n_individos):
            populacao.append(self.gera_individos())
        return populacao

    def crossover(self, paiA, paiB):
        proxima_geracao = []

        proxima_geracao.append(paiA)
        proxima_geracao.append(paiB)

        while len(proxima_geracao) < self.n_individos:
            ponto_cruzamento = random.randint(0, len(paiA) - 1)
            novo_filho = paiA[:ponto_cruzamento] + paiB[ponto_cruzamento:]
            novo_filho_num = [float(i) for i in novo_filho]
            proxima_geracao.append(novo_filho_num)
        return proxima_geracao

    def mutacao(self, populacao, taxa_mutacao=0.20):
        for individuo in populacao:
            if random.random() < taxa_mutacao:
                pontoMutacao = random.randint(0, len(individuo) - 1)
                individuo[pontoMutacao] = random.uniform(self.menor_valor_crom, self.maior_valor_crom)
        return populacao
