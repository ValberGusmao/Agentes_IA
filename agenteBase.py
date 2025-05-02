from abc import ABC, abstractmethod
import random

class AgenteBase(ABC):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
    
    def explorar(self, ambiente):
        visao = self.verAmbiente(ambiente)
        novaPos = self.movimentacao(visao)
        self.x, self.y = novaPos
        print((self.x, self.y))
    
    def movimentacao(self, visao):
        maior = 0
        opcoes = []
        for (x, y, valor) in visao:
            if valor > maior:
                maior = valor
                pos = (x, y)
            elif (self.x - x == 0 or self.y - y ==0):
                opcoes.append((x, y))
        
        if maior != 0:
            print("Recurso")
            opcoes = [(pos[0], self.y), (self.x, pos[1])]
            return self.escolherAleatorio(opcoes)
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
        elementoMapa = ambiente.pegarElemento(self.x, self.y)

    # Agente
    #     AgenteSimples
    #     AgenteComMemoria
    #         Cooperativo
    #         objetivo
    #         Estados
    #         BCI
    