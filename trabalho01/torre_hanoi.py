#!/usr/bin/env python

from problema import Problema


class ProblemaTorreHanoi(Problema):
    
    class Estado(object):
        def __init__(self):
            self.torre_a = []
            self.torre_b = []
            self.torre_c = []
            self.pai = None
            self.acao = ''

        def copy(self):
            estado = ProblemaTorreHanoi.Estado()
            estado.torre_a = self.torre_a.copy()
            estado.torre_b = self.torre_b.copy()
            estado.torre_c = self.torre_c.copy()
            return estado

        def __repr__(self):
            return f'Torre A: {self.torre_a}\nTorre B: {self.torre_b}\nTorre C: {self.torre_c}\n'

        def __eq__(self, estado):
            return self.torre_a == estado.torre_a and self.torre_b == estado.torre_b and self.torre_c == estado.torre_c

    @property
    def estado_inicial(self):
        estado = ProblemaTorreHanoi.Estado()
        estado.torre_a = [5, 4, 3, 2, 1]
        estado.torre_b = []
        estado.torre_c = []
        estado.pai = None
        return estado

    def funcao_objetivo(self, estado):
        return estado.torre_c == [5, 4, 3, 2, 1]

    def solucao(self, estado):
        solucao_final = []
        while estado.pai is not None:
            solucao_final.append(estado)
            estado = estado.pai
        solucao_final.append(estado)

        return solucao_final#.reverse()

    def __mover(self, estado_pai, acao):
        
        estado = estado_pai.copy()
        estado.acao = acao
        
        tamanhoA = len(estado.torre_a)
        tamanhoB = len(estado.torre_b)
        tamanhoC = len(estado.torre_c)
        
        if acao == 'AB' and tamanhoA > 0 and (tamanhoB == 0 or estado.torre_a[tamanhoA - 1] < estado.torre_b[tamanhoB - 1]):
            estado.torre_b.append(estado.torre_a.pop(-1))
            estado.pai = estado_pai

        elif acao == 'AC' and tamanhoA > 0 and (tamanhoC == 0 or estado.torre_a[tamanhoA - 1] < estado.torre_c[tamanhoC - 1]):
            estado.torre_c.append(estado.torre_a.pop(-1))
            estado.pai = estado_pai

        elif acao == 'BA' and tamanhoB > 0 and (tamanhoA == 0 or estado.torre_b[tamanhoB - 1] < estado.torre_a[tamanhoA - 1]):
            estado.torre_a.append(estado.torre_b.pop(-1))
            estado.pai = estado_pai

        elif acao == 'BC' and tamanhoB > 0 and (tamanhoC == 0 or estado.torre_b[tamanhoB - 1] < estado.torre_c[tamanhoC - 1]):
            estado.torre_c.append(estado.torre_b.pop(-1))
            estado.pai = estado_pai

        elif acao == 'CA' and tamanhoC > 0 and (tamanhoA == 0 or estado.torre_c[tamanhoC - 1] < estado.torre_a[tamanhoA - 1]):
            estado.torre_a.append(estado.torre_c.pop(-1))
            estado.pai = estado_pai

        elif acao == 'CB' and tamanhoC > 0 and (tamanhoB == 0 or estado.torre_c[tamanhoC - 1] < estado.torre_b[tamanhoB - 1]):
            estado.torre_b.append(estado.torre_c.pop(-1))
            estado.pai = estado_pai

        else:
            return None

        return estado

    def funcao_sucessora(self, estado):
        sucessores = []
        a1 = self.__mover(estado, 'AB')
        a2 = self.__mover(estado, 'AC')
        a3 = self.__mover(estado, 'BA')
        a4 = self.__mover(estado, 'BC')
        a5 = self.__mover(estado, 'CA')
        a6 = self.__mover(estado, 'CB')

        if a1: sucessores.append(a1)
        if a2: sucessores.append(a2)
        if a3: sucessores.append(a3)
        if a4: sucessores.append(a4)
        if a5: sucessores.append(a5)
        
        return sucessores
