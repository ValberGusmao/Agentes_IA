from abc import ABC, abstractmethod
from enum import Enum
import random

class AgenteBase(ABC):

    class EstadosAgente(Enum):
        ANDANDO = 1
        COLETANDO = 2
        VOLTANDO_BASE = 3

    def __init__(self, simbolo:str, x, y):
        super().__init__()

        self.estado = self.EstadosAgente.ANDANDO
        self.simbolo = simbolo
        self.carga = 0
        self.x = x
        self.y = y

    def __str__(self):
        return self.simbolo
    
    def explorar(self, ambiente):
        if self.estado == self.EstadosAgente.ANDANDO:
            visao = self.verAmbiente(ambiente)
            novaPos = self.movimentacao(visao)
            if novaPos != None:
                ambiente.moverEntidade(novaPos[0], novaPos[1], self)
                self.x, self.y = novaPos
        elif self.estado == self.EstadosAgente.COLETANDO:
            #visao = self.verAmbiente(ambiente)
            self.coletarRecurso(ambiente)
        else: #VoltandoBase
           self.voltarBase()
    
    def movimentacao(self, visao):
        pass

    def escolherAleatorio(self, lista):
        if lista:
            return random.choice(lista)
        return None

    def voltarBase(self, ambiente):
        pos_base = ambiente.get_pos_base()

        #anda um passo na direção da base
        if self.x < pos_base[0]:
            novo_x = self.x + 1
        elif self.x > pos_base[0]:
            novo_x = self.x - 1
        else:
            novo_x = self.x

        if self.y < pos_base[1]:
            novo_y = self.y + 1
        elif self.y > pos_base[1]:
            novo_y = self.y - 1
        else:
            novo_y = self.y

        if ambiente.moverEntidade(novo_x, novo_y, self):
            self.x = novo_x
            self.y = novo_y

        # Chegou na base
        if (self.x, self.y) == pos_base:
            print(f"{self.simbolo} entregou recurso na base!")
            self.carga = 0
            self.estado = self.EstadosAgente.ANDANDO

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
        valor = ambiente.removerRecurso(self.x, self.y)

        if valor == -2:
            print("Estrutura encontrada, aguardando agente auxiliar...")
            self.estado = self.EstadosAgente.ANDANDO  # ou um estado tipo "ESPERANDO"
        elif valor > 0:
            self.carga = valor
            print("Recurso Coletado")
            self.estado = self.EstadosAgente.VOLTANDO_BASE
        elif valor == 0:
            print("Recurso não encontrado")
            self.estado = self.EstadosAgente.ANDANDO
        else:
            print("Extraindo recurso...")

    # Agente
    #     AgenteSimples
    #     AgenteComMemoria
    #         Cooperativo
    #         objetivo
    #         Estados
    #         BCI
    