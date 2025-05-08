from enum import Enum
import random
from tipoTerreno import Tipo

class AgenteBase():

    class EstadosAgente(Enum):
        ANDANDO = 1
        COLETANDO = 2
        VOLTANDO_BASE = 3

    def __init__(self, simbolo:str, pos:tuple[int, int]):
        super().__init__()

        self.estado = self.EstadosAgente.ANDANDO
        self.simbolo = simbolo
        self.carga = 0
        self.x, self.y = pos 
    
    def explorar(self, ambiente):
        if self.estado == self.EstadosAgente.ANDANDO:
            visao = self.verAmbiente(ambiente)
            novaPos = self.movimentacao(visao)
            self.deslocarAgente(ambiente, novaPos)
        
        elif self.estado == self.EstadosAgente.COLETANDO:
            self.coletar(ambiente)
        
        elif self.estado == self.EstadosAgente.VOLTANDO_BASE: #VoltandoBase   
            # Chegou na base
            novaPos = self.irAte(ambiente.posBase)
            self.deslocarAgente(ambiente, novaPos)
            if novaPos == ambiente.posBase:
                print(f"{self.simbolo} entregou recurso na base!")
                self.carga = 0
                self.estado = self.EstadosAgente.ANDANDO
    
        else: #No estado AGURDANDO
            pass
        #Talvez ele poderia mandar uma mensagem pedindo ajuda aos outros agentes
    
    def movimentacao(self, visao) -> tuple[int, int]:
        pass

    def deslocarAgente(self, ambiente, pos):
        if pos != None:
            ambiente.moverAgente(pos[0], pos[1], self)
            self.x, self.y = pos

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

    
    def verAmbiente(self, ambiente) -> list:
        visao = []
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (j != 0 or k != 0): #Não pegar o elemento do meio
                    posX, posY = j + self.x, k + self.y
                    aux = ambiente.getElemento(posX, posY)
                    if aux != None:
                        visao.append((posX, posY, aux))    
        return visao
    
    #Compara duas posições e verifica se uma está na diagonal da outra.
        #Caso esteja na diagonal, retorna um valor em linha reta que mistura as duas posições
        #Caso estejam em linha reta, retorna o valor de nextPos
    def quebrarDiagonal(self, initPos: tuple[int, int], nextPos:tuple[int, int]) ->tuple[int, int]:
        if initPos[0] - nextPos[0] != 0 and initPos[1] - nextPos[1] != 0:
            opcoes = [(nextPos[0], initPos[1]), (initPos[0], nextPos[1])]
            return self.escolherAleatorio(opcoes)
        else:
            return nextPos
    
    #Retorna a próxima posição que o agente precisa se mover para se aproximar do objetico
    def irAte(self, posObjetivo) -> tuple[int, int]:
        pos = (posObjetivo[0] - self.x, posObjetivo[1] - self.y)
        pos = list(pos)

        for i in range(2):
            if pos[i] > 1:
                pos[i] = 1
            elif pos[i] < -1:
                pos[i] = -1
        
        res = self.quebrarDiagonal((0, 0), pos)
        if pos != res:
            pos = (res[0], res[1])

        return (pos[0] + self.x, pos[1] + self.y)
        
    def escolherAleatorio(self, lista) -> any:
        if lista:
            return random.choice(lista)
        return None

    def __str__(self):
        return self.simbolo

    # Agente
    #     AgenteSimples
    #     AgenteComMemoria
    #         Cooperativo
    #         objetivo
    #         Estados
    #         BCI
    