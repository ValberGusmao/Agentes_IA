import pygame

from tipoTerreno import Tipo

class View():

    colorMap = {
        Tipo.LIVRE: (255, 255, 255),        # branco
        Tipo.RIO: (0, 255, 255),            # ciano
        Tipo.BASE: (255, 255, 0),           # amarelo
        Tipo.CRISTAL: (255, 0, 255),        # roxo
        Tipo.METAL: (111, 111, 111),        # cinza
        Tipo.ESTRUTURA: (255, 0, 0),        # vermelho
    }

    def __init__(self, tamX, tamY, cellSize):
        # Dimensões da janela
        self.cellSize = cellSize
        self.largura = tamX * cellSize
        self.altura = tamY * cellSize

        # Inicializar pygame
        pygame.init()
        self.pygameDisplay = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Planeta Desconhecido")

    def exibir(self, ambiente, bdi):
        self.pygameDisplay.fill((0, 0, 0))
        self.desenhar_grid(ambiente)
        #self.desenharApenasDescobertos(ambiente, bdi)
        pygame.display.flip()

    def fecharTela(self):
        pygame.quit()

    def adicionarElementoVisual(self, chave:str, color:tuple[int, int, int]):
        View.colorMap[chave] = color

    def desenharApenasDescobertos(self, ambiente, bdi):
        altura = min(self.altura // self.cellSize, ambiente.altura)
        largura = min(self.largura // self.cellSize, ambiente.largura)

        for i in range(altura):
            for j in range(largura):
                eleMapa = ambiente.mapa[i][j].getElemento()

                if not isinstance(eleMapa, Tipo):
                    cor = self.colorMap[eleMapa.simbolo]

                elif (j, i) in bdi.recursosConhecidos:
                    if eleMapa in self.colorMap:
                        cor = self.colorMap[eleMapa]
                else:
                    cor = self.colorMap[Tipo.LIVRE]
                pygame.draw.rect(self.pygameDisplay, cor, (j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize))  # posição
                pygame.draw.rect(self.pygameDisplay, (200, 200, 200), (j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize), 1)  # contorno do grid

    def desenhar_grid(self, ambiente):
        altura = min(self.altura // self.cellSize, ambiente.altura)
        largura = min(self.largura // self.cellSize, ambiente.largura)

        for i in range(altura):
            for j in range(largura):
                eleMapa = ambiente.mapa[i][j].getElemento()

                if eleMapa in self.colorMap:
                    cor = self.colorMap[eleMapa]
                elif eleMapa.simbolo in self.colorMap:
                    cor = self.colorMap[eleMapa.simbolo]
                else:
                    cor = (0, 0, 0)

                pygame.draw.rect(self.pygameDisplay, cor, (j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize))  # posição
                pygame.draw.rect(self.pygameDisplay, (200, 200, 200), (j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize), 1)  # contorno do grid
