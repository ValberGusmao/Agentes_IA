import random

from elementoMapa import ElementoMapa
from tipoTerreno import Tipo 

class Ambiente:
    def __init__(self, altura:int, largura:int):
        self.mapa = self.criarMapa(altura, largura)
        self.recursosRestantes:int = 0
        self.largura = largura
        self.altura = altura
        self.agentes = []
        self.posBase = None  # Armazena posição da base como tupla (x, y)

    def criarMapa(self, altura:int, largura:int) -> list[list[ElementoMapa]]:
        mapa = []
        for _ in range(altura):
            linha = []
            for _ in range(largura):
                linha.append(ElementoMapa())
            mapa.append(linha)
        return mapa

    def adicionarAgente(self, agente):
        pos = self.getElemento(agente.x, agente.y)
        if pos != None:
            pos.adicionarAgente(agente)
        else:
            raise ValueError(f"Posição ({agente.x}, {agente.y}) inválida para adicionar Agente.")
    
    def moverAgente(self, x:int, y:int, agente):
        oldX, oldY = agente.x, agente.y
        proximaPos = self.getElemento(x, y)
        if proximaPos != None:
            self.getElemento(oldX, oldY).moverAgente(agente, proximaPos)
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida para mover o agente.")

    def adicionarBase(self, x:int, y:int):
        if self.posBase == None:
            pos = self.getElemento(x, y)
            if pos != None:
                self.posBase = (x, y)  # ← Aqui é onde armazenamos a posição da base
                pos.posicionarElemento(Tipo.BASE)
            else:
                raise ValueError(f"Posição ({x}, {y}) inválida para adicionar Base.")
        else:
            raise ValueError("Já há uma base posicionada nesse ambiente.")
       
    def preencherMapa(self, elemento:Tipo, quantidade:int):
        count = 0
        while count < quantidade:
            i = random.randint(0, self.altura - 1)
            j = random.randint(0, self.largura - 1)
            if self.mapa[i][j].terreno == Tipo.LIVRE:
                self.mapa[i][j].posicionarElemento(elemento)
                count += 1
        self.recursosRestantes = count

    def adicionarRecurso(self, x:int, y:int, recurso:Tipo):
        pos = self.getElemento(x, y)
        if pos != None:
            pos.posicionarElemento(recurso)
            self.recursosRestantes += 1
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida para adicionar recurso.")

    def removerRecurso(self, x:int, y:int) -> ElementoMapa:
        pos = self.getElemento(x, y)
        if pos != None:
            return pos.coletarRecurso()
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida no mapa.")
        
    def getElemento(self, x:int, y:int) -> ElementoMapa:
        if self.posValida(y, x):
            return self.mapa[y][x]
        return None
        
    def get_pos_base(self) -> tuple[int, int]:
        if self.posBase != None:
            return self.posBase
        else:
            raise ValueError("A base ainda não foi posicionada.")
    
    def posValida(self, x:int, y:int) -> bool:
        return (0 <= x < self.altura) and (0 <= y < self.largura)
    
    def printMapa(self):
        for linha in range(len(self.mapa)):
            print(" ".join(map(str, self.mapa[linha])))