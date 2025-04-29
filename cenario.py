class Cenario:
    mapa = []

    def cria_mapa(self, tamX, TamY):
        
        for linha in range(TamY):
            linha = []
            for coluna in range(tamX):
                linha.append(0)
            self.mapa.append(linha)
        self.printMapa()

    def printMapa(self):
        for linha in self.mapa:
            print(linha)