import random

from elementoMapa import ElementoMapa
from tipoTerreno import Tipo 

class Ambiente:
    def __init__(self, largura, altura):
        self.mapa = self.criarMapa(largura, altura)
        self.largura = largura
        self.altura = altura
        self.basePosicionada:bool = False
        self.entidades = [] #Entidades são elementos que podem se mover pelo mapa
        self.pos_base = None  # Armazena posição da base como tupla (x, y)

    #Entidade != Estrutura/Terreno

    def ecriarMapa(self, tamX, tamY):
        mapa = []
        for li in range(tamX):
            linha = []
            for col in range(tamY):
                linha.append(ElementoMapa())
            mapa.append(linha)
        return mapa

    def getElemento(self, x:int, y:int):
        if self.posValida(x, y):
            return (x, y, self.mapa[x][y])
        return None
    
    def adicionarEntidade(self, entidade):
        x = entidade.x
        y = entidade.y
        if self.posValida(x, y):
            self.mapa[x][y].adicionarEntidade(entidade)
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida para adicionar entidade.")
    
    def moverEntidade(self, x, y, entidade):
        if self.posValida(x, y):
            self.mapa[entidade.x][entidade.y].moverEntidade(entidade, self.mapa[x][y])

    def adicionarBase(self, x, y):
        if self.posValida(x, y):
            if not self.basePosicionada:
                self.mapa[x][y].posicionarElemento(Tipo.BASE)
                self.basePosicionada = True
                self.pos_base = (x, y)  # ← Aqui é onde armazenamos a posição da base
            else:
                raise ValueError("Já há uma base posicionada nesse ambiente.")
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida para adicionar Base.")

    def preencherMapa(self, elemento, quantidade):
        count = 0
        while count < quantidade:
            i = random.randint(0, self.largura - 1)
            j = random.randint(0, self.altura - 1)
            if self.mapa[i][j].terreno == Tipo.LIVRE:
                self.mapa[i][j].posicionarElemento(elemento)
                count += 1

    def adicionarRecurso(self, x, y, recurso):
        if self.posValida(x, y):
            self.mapa[x][y].posicionarElemento(recurso)
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida para adicionar recurso.")

    def removerRecurso(self, x, y):
        if self.posValida(x, y):
            return self.mapa[x][y].coletarRecurso()
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida no mapa.")

    def posValida(self, x:int, y:int):
        return (0 <= x < self.largura) and (0 <= y < self.altura)

    def printMapa(self):
        for linha in range(len(self.mapa)):
            print(" ".join(map(str, self.mapa[linha])))

    def get_pos_base(self):
        if self.basePosicionada and self.pos_base is not None:
            return self.pos_base
        else:
            raise ValueError("A base ainda não foi posicionada.")

    def tipo_recurso(self, x, y):
        if self.posValida(x, y):
            tipo = self.mapa[x][y].terreno
            if tipo in [Tipo.CRISTAL, Tipo.METAL, Tipo.ESTRUTURA]:
                return tipo
            else:
                return None  #nao eh recurso
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida no mapa.")
