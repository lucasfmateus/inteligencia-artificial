#!/usr/bin/env python

from pprint import pprint
from typing import List
from problema import Problema


class BuscaEmProfundidade(object):

    # TODO: verificar objeto None sendo retornado
    def busca_profundidade(self, problema: Problema, estado=None, visitados=[]):

        if estado is None:
            estado = problema.estado_inicial

        #print(f'> Estado sendo avaliado:')
        #print(f'{estado}')

        if problema.funcao_objetivo(estado):
            print('\n >>>> Solucao encontrada <<<< \n')
            return estado

        sucessores = problema.funcao_sucessora(estado)

        # Executa a busca recursivamente
        for sucessor in sucessores:

            if not visitados.__contains__(sucessor):
                visitados.append(sucessor)
                estado_recursivo = self.busca_profundidade(problema, sucessor, visitados)

                if estado_recursivo is not None:
                    if problema.funcao_objetivo(estado_recursivo):
                        return estado_recursivo
                #    else:
                #        return sucessor.pai

        return None
