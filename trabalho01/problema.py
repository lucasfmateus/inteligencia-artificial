#!/usr/bin/env python
class Problema(object):
    """Classe que representa a definicao de um problema. Deve ser usada
    como base para a definicao dos problemas.
    """

    @property
    def estado_inicial(self):
        """Retorna o estado inicial do problema."""
        raise RuntimeError('Funcao nao implementada.')

    def solucao(self, estado):
        """Gera uma lista com a solucao de um problema a partir de um estado."""
        raise RuntimeError('Funcao nao implementada.')

    def funcao_objetivo(self, estado):
        """Verifica se a funcao atingiu o seu objetivo."""
        raise RuntimeError('Funcao nao implementada.')

    def funcao_sucessora(self, estado):
        """Gera os estados sucessores a partir de um estado."""
        raise RuntimeError('Funcao nao implementada.')