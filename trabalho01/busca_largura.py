#!/usr/bin/env python
from pprint import pprint
from typing import List

from problema import Problema


class Buscalargura():

    def busca_largura(self, problema: Problema):
        """Agente que implementa a busca em largura
        :param problema: definicao do problema
        :return: lista com os estados para chegar na solucao do problema
        """

        # 1. Adiciona o estado inicial na lista de borda
        borda = [problema.estado_inicial]

        # Cria uma lista com a memoria dos estados ja visitados
        memoria = [problema.estado_inicial]

        while True:

            # 2. Verifica se houve falha
            if not borda:
                print('Falha ao encontrar solucao')
                return []

            # 3. Recupera o proximo estado
            estado = borda.pop(0)
            print(f'=' * 80)
            print(f'> Estado sendo avaliado:')
            print(f'{estado}')

            # 4. Verifica se achou a solucao objetivo
            if problema.funcao_objetivo(estado):
                print('Solucao encontrada.')
                return problema.solucao(estado)

            # 5. Geracao dos estados sucessores
            # ** Na busca em largura, os estados sucessores sao adicionados
            # ** ao final da lista
            sucessores = problema.funcao_sucessora(estado)
            borda.extend([x for x in sucessores if x not in memoria])

            memoria.extend([x for x in sucessores if x not in memoria])

            # print('-'*80)
            #print('sucessores:')
            #for x in sucessores:
            #    print(x)
            ##
            #print('*-*' * 80)
            #print('memoria:')
            #for x in memoria:
            #    print(x)
            #print()


            # Adiciona os novos estados gerados na memoria
            memoria.extend(sucessores)

            print(f'> Estados sucessores: {len(sucessores)}')
