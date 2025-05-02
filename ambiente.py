class Ambiente:
    def __init__(self, largura, altura):
        self.mapa = self.criarMapa(largura, altura)
        self.largura = largura
        self.altura = altura
        self.entidades = [] #Entidades são elementos que podem se mover pelo mapa
    
    #Entidade != Recurso/Estrutura != Terreno

    def criarMapa(self, tamX, tamY):
        mapa = []
        for li in range(tamX):
            linha = []
            for col in range(tamY):
                linha.append(0)
            mapa.append(linha)
        return mapa

    def pegarElemento(self, x:int, y:int):
        if (0 <= x < self.largura) and (0 <= y < self.altura):
            return (x, y, self.mapa[x][y])
        else:
            return None
    
    def adicionarEntidade(self, x, y, entidade):
        pass

    def adicionarRecurso(self):
        pass

    def printMapa(self):
        for linha in range(len(self.mapa)):
            print(" ".join(map(str, self.mapa[linha])))