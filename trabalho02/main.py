#!/usr/bin/env python

from pprint import pprint
from labirinto import Labirinto
from busca_largura import BuscaLargura
from busca_gulosa import BuscaGulosa

def main():
    # Definicao do problema do labirinto
    problema = Labirinto()

    #busca = BuscaLargura()
    #solucao = busca.busca_em_largura(problema)

    busca = BuscaGulosa()
    solucao = busca.busca_gulosa(problema)

    pprint(problema.solucao(solucao))


if __name__ == '__main__':
    main()
