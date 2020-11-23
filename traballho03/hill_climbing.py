#!/usr/bin/env python


class HillClimbing(object):

    def __init__(self, max_alt, max_sem_alt):
        self.max_alt = max_alt
        self.max_sem_alt = max_sem_alt

    def executa(self, problema):
        atual = problema.estado_inicial
        i = 0
        j = 0

        while i < self.max_alt or j < self.max_sem_alt:
            print(f"{i:03d} - {atual} - {problema.funcao_objetivo(atual)}")

            vizinho = problema.funcao_sucessora(atual)
            custo_atual = problema.funcao_objetivo(atual)
            custo_vizinho = problema.funcao_objetivo(vizinho)

            if custo_vizinho < custo_atual:

                print(f'achou melhor! atual = {custo_atual}  vizinho {custo_vizinho}')
                atual = vizinho

                j = 0

            i += 1
            j += 1