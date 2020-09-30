#!/usr/bin/env python
from pprint import pprint
from typing import List

from problema import Problema
from labirinto import Labirinto


class BuscaGulosa(object):

    def busca_gulosa(self, problema: Labirinto):
        """Agente que implementa a busca em gulosa:
            :param problema: definicao do problema
            :return: lista com os estados para chegar na solucao do problema
        """

        # Busca estados sucessores
        # Escolhe o melhor estado sucessor
        #   - O melhor estado é aquele que mais se aproxima da saída
        #   - Quanto mais abaixo e mais a direita, mais próximo da saída

        atual = problema.estado_inicial
        visitados = [problema.estado_inicial]

        while True:

            print(f'=' * 80)
            print(f'> Estado sendo avaliado:')
            print(f'{atual}')

            # Verifica se achou a solucao objetivo
            if problema.funcao_objetivo(atual):
                print('Solucao encontrada.')
                #return problema.solucao(atual)
                return atual
            # Geracao dos estados sucessores
            sucessores = problema.funcao_sucessora(atual)

            aux = atual.copy()

            # Escolhe o melhor estado dentre os estados sucessores gerados
            for sucessor in sucessores:
                if sucessor > atual and not visitados.__contains__(sucessor):  # Também verifica se o estado ja foi visitado, evitando loops
                    atual = sucessor.copy()

            visitados.append(atual)

            # Se não encontrou um sucessor melhor, volta para o estado pai
            if atual == aux:
                atual = atual.pai

                # Caso tenha voltado até a raiz, não encontrou a solução
                if atual is None:
                    print('Solucao não encontrada.')
                    return None

            # print('-'*80)
            #print('Sucessores:')

            #for x in sucessores:
            #    print(x)

            #print(f'Escolhido: {atual}')
            #print(f'> Estados sucessores: {len(sucessores)}')
