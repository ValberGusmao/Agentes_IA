from enum import Enum
import random
from tipoTerreno import Tipo

class AgenteBase():

    class EstadosAgente(Enum):
        ANDANDO = 1
        COLETANDO = 2
        AGUARDANDO = 3 #O agente está esperando para explorar a estrutura
        VOLTANDO_BASE = 4

    def __init__(self, simbolo:str, x, y):
        super().__init__()

        self.estado = self.EstadosAgente.ANDANDO
        self.simbolo = simbolo
        self.carga = 0
        self.x = x
        self.y = y
    
    def explorar(self, ambiente):
        if self.estado == self.EstadosAgente.ANDANDO:
            visao = self.verAmbiente(ambiente)
            novaPos = self.movimentacao(visao)
            if novaPos != None:
                ambiente.moverAgente(novaPos[0], novaPos[1], self)
                self.x, self.y = novaPos
        elif self.estado == self.EstadosAgente.COLETANDO:
            self.coletar(ambiente)
        elif self.estado == self.EstadosAgente.VOLTANDO_BASE: #VoltandoBase
           self.voltarBase(ambiente)
        else: #No estado AGURDANDO
            self.coletandoEstrutura(ambiente)
        #Talvez ele poderia mandar uma mensagem pedindo ajuda aos outros agentes
    
    def movimentacao(self, visao):
        pass

    def escolherAleatorio(self, lista):
        if lista:
            return random.choice(lista)
        return None

    def voltarBase(self, ambiente):
        pos_base = ambiente.get_pos_base()
        
        # Move primeiro em x
        if self.x < pos_base[0]:
            novo_x = self.x + 1
            novo_y = self.y
        elif self.x > pos_base[0]:
            novo_x = self.x - 1
            novo_y = self.y
        else:
            # Depois move em y
            if self.y < pos_base[1]:
                novo_x = self.x
                novo_y = self.y + 1
            elif self.y > pos_base[1]:
                novo_x = self.x
                novo_y = self.y - 1
            else:
                # Já esta na base
                novo_x, novo_y = self.x, self.y
        
        ambiente.moverAgente(novo_x, novo_y, self)
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
                    posX, posY = j + self.x, k + self.y
                    aux = ambiente.getElemento(posX, posY)
                    if aux != None:
                        visao.append((posX, posY, aux))    
        return visao

    def coletar(self, ambiente):
        valor, tipo = ambiente.coletarRecurso(self.x, self.y)

        if valor > 0:
            self.carga = valor
            print("Recurso Coletado")
            self.estado = self.EstadosAgente.VOLTANDO_BASE
        elif tipo == Tipo.ESTRUTURA: #valor 0 e tipo ESTRUTURA
            print("Estrutura encontrada, aguardando agente auxiliar...")
            #self.estado = self.EstadosAgente.AGUARDANDO
        elif valor == 0:
            print("Recurso não encontrado")
            self.estado = self.EstadosAgente.ANDANDO

    def __str__(self):
        return self.simbolo

    # Agente
    #     AgenteSimples
    #     AgenteComMemoria
    #         Cooperativo
    #         objetivo
    #         Estados
    #         BCI
    