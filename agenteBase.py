from enum import Enum
import random
from tipoTerreno import Tipo

class Carga():
    def __init__(self):
        self.x:int = 0
        self.y:int = 0
        self.valor:int = 0

class AgenteBase():

    class EstadosAgente(Enum):
        ANDANDO = 1
        COLETANDO = 2
        VOLTANDO_BASE = 3 

    def __init__(self, simbolo:str, pos:tuple[int, int], BDI):
        super().__init__()

        self.estado = self.EstadosAgente.ANDANDO
        self.simbolo = simbolo
        self.x, self.y = pos 
        self.BDI = BDI

        self.pontuacao = 0
        self.quantidadeRecursos = 0
        self.carga = Carga()
    
    def explorar(self, ambiente):
        visao = self.verAmbiente(ambiente)
        recursos = self.verificarRecursos(visao)
        
        if self.estado == self.EstadosAgente.ANDANDO:
            novaPos = self.movimentacao(recursos, visao)
            self.deslocarAgente(ambiente, novaPos)
        
        elif self.estado == self.EstadosAgente.COLETANDO:
            self.coletar(ambiente)
        
        elif self.estado == self.EstadosAgente.VOLTANDO_BASE: #VoltandoBase   
            # Chegou na base
            novaPos = self.irAte(ambiente.posBase)
            self.deslocarAgente(ambiente, novaPos)
            if novaPos == ambiente.posBase:
                self.entrouNaBase(ambiente, self.carga)
    

    def verificarRecursos(self, visao) -> tuple[int, int, any]:
        recursosVistos = []
        for (x, y, elementoMapa) in visao:
            valor = elementoMapa.terreno.value.valor
            # para guardar o local do recurso em um conjunto assim que ve
            if valor > 0:
                recursosVistos.append((x, y, elementoMapa))
        return recursosVistos


    #Os agentes Simples e com Estado estão complementando essa função com a interação com o BDI
    def entrouNaBase(self, ambiente, carga:Carga):
        self.estado = self.EstadosAgente.ANDANDO
        if carga.valor > 0:
            self.pontuacao += self.carga.valor
            self.quantidadeRecursos += 1
            self.BDI.depositarCarga(carga)
        self.carga.valor = 0

        # print(f"{self.simbolo} entregou recurso na base!")        

    #Os outros agentes definem essa função
    def movimentacao(self, visao) -> tuple[int, int]:
        pass

    def deslocarAgente(self, ambiente, pos):
        if pos != None:
            ambiente.moverAgente(pos[0], pos[1], self)
            self.x, self.y = pos

    def coletar(self, ambiente):
        valor, tipo = ambiente.coletarRecurso(self.x, self.y)

        if valor > 0:
            self.carga.x = self.x
            self.carga.y = self.y
            self.carga.valor = valor
            # print("Recurso Coletado")
            self.estado = self.EstadosAgente.VOLTANDO_BASE
        elif tipo == Tipo.ESTRUTURA: #valor 0 e tipo ESTRUTURA
            # print("Estrutura encontrada, aguardando agente auxiliar...")
            mensagem = {
            'tipo': Tipo.ESTRUTURA,
            'posicao': (self.x, self.y),
        }
            self.enviarMensagem(mensagem)

        elif valor == 0:
            # print("Recurso não encontrado")
            self.estado = self.EstadosAgente.ANDANDO

        return (valor, tipo)

    
    def verAmbiente(self, ambiente) -> list:
        visao = []
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (j != 0 or k != 0): #Não pegar o elemento do meio
                    posX, posY = j + self.x, k + self.y
                    elemento = ambiente.getElemento(posX, posY)
                    if elemento != None:
                        visao.append((posX, posY, elemento))    
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
    
    def enviarMensagem(self, conteudo):
        # print("Agente qualquer: enviando posicao de uma estrutura...")
        self.BDI.receberMensagemBDI(conteudo)

    def printMetricas(self):
        print(f"O {self.__class__.__name__} pegou {self.quantidadeRecursos} recursos e obteve a pontuação de {self.pontuacao}")

    def __str__(self):
        return self.simbolo
    
    # Agente
    #     AgenteSimples
    #     AgenteComMemoria
    #         Cooperativo
    #         objetivo
    #         Estados
    #         BCI