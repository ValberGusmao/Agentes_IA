from elementoMapa import ElementoMapa

class Ambiente:
    def __init__(self, largura, altura):
        self.mapa = self.criarMapa(largura, altura)
        self.largura = largura
        self.altura = altura
        self.entidades = [] #Entidades são elementos que podem se mover pelo mapa
    
    #Entidade != Estrutura/Terreno

    def criarMapa(self, tamX, tamY):
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
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida no mapa.")
    
    def adicionarEntidade(self, x, y, entidade):
        if self.posValida(x, y):
            self.mapa[x][y].adicionarEntidade(entidade)
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida para adicionar entidade.")
    
    def adicionarRecurso(self, x, y, recurso):
        if self.posValida(x, y):
            self.mapa[x][y].adicionarRecurso(recurso)
        else:
            raise ValueError(f"Posição ({x}, {y}) inválida para adicionar recurso.")

    def moverEntidade(self, x, y, entidade):
        if self.posValida(x, y):
            self.mapa[entidade.x][entidade.y].moverEntidade(entidade, self.mapa[x][y])

    def posValida(self, x:int, y:int):
        return (0 <= x < self.largura) and (0 <= y < self.altura)

    def printMapa(self):
        for linha in range(len(self.mapa)):
            print(" ".join(map(str, self.mapa[linha])))