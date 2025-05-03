from abc import ABC, abstractmethod
import random

class AgenteBase(ABC):

    def __init__(self, simbolo:str, x, y):
        super().__init__()
        self.simbolo = simbolo
        self.x = x
        self.y = y
        self.carga = 0

    def __str__(self):
        return self.simbolo
    
    def explorar(self, ambiente):
        if ambiente.getElemento(self.x, self.y)[2].terreno.value.valor > 0:
            self.coletarRecurso(ambiente)
        else:
            visao = self.verAmbiente(ambiente)
            novaPos = self.movimentacao(visao)
            ambiente.moverEntidade(novaPos[0], novaPos[1], self)
            self.x, self.y = novaPos
    
    def movimentacao(self, visao):
        maior = 0
        opcoes = []
        for (x, y, elementoMapa) in visao:
            valor = elementoMapa.terreno.value.valor
            if valor > maior:
                maior = valor
                pos = (x, y)
            elif (self.x - x == 0 or self.y - y ==0):
                opcoes.append((x, y))
        
        if maior != 0:
             #O recurso tá na diagonal. É agente tem que escolher entre duas opções em linha reta
            if self.x - pos[0] != 0 and self.y - pos[1] != 0:
                opcoes = [(pos[0], self.y), (self.x, pos[1])]
                return self.escolherAleatorio(opcoes)
            return pos
        else:
            res = self.escolherAleatorio(opcoes)
            return (res[0], res[1])

    def escolherAleatorio(self, lista):
        if lista:
            return random.choice(lista)
        return None

    def voltarBase():
        pass

    def verAmbiente(self, ambiente):
        visao = []
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (j != 0 or k != 0): #Não pegar o elemento do meio
                    aux = ambiente.getElemento(j + self.x, k + self.y)
                    if aux != None:
                        visao.append(aux)    
        return visao 

    def coletarRecurso(self, ambiente):
        self.carga = ambiente.removerRecurso(self.x, self.y)
        print("Recurso Coletado")

    # Agente
    #     AgenteSimples
    #     AgenteComMemoria
    #         Cooperativo
    #         objetivo
    #         Estados
    #         BCI
    