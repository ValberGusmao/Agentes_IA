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
        self.altura = tamX * cellSize
        self.largura = tamY * cellSize

        # Inicializar pygame
        pygame.init()
        self.pygameDisplay = pygame.display.set_mode((self.altura, self.largura))
        pygame.display.set_caption("Planeta Desconhecido")

        # Inicializar fonte
        pygame.font.init()
        self.fonte = pygame.font.SysFont('Arial', 20)

    def exibir(self, ambiente, tempoRestante):
        self.pygameDisplay.fill((0, 0, 0))
        self.desenhar_grid(ambiente)

        # Renderizar o tempo restante na tela
        texto_tempo = self.fonte.render(f"Tempo restante: {tempoRestante}s", True, (0, 0, 0))
        self.pygameDisplay.blit(texto_tempo, (10, 10))
        pygame.display.flip()

        pygame.time.Clock().tick(10)

    def fecharTela(self):
        pygame.quit()

    def adicionarElementoVisual(self, chave:str, color:tuple[int, int, int]):
        View.colorMap[chave] = color

    def desenhar_grid(self, ambiente):
        for i in range(len(ambiente.mapa)):
            for j in range(len(ambiente.mapa[0])):
                eleMapa = ambiente.mapa[i][j].getElemento()

                if eleMapa in self.colorMap:
                    cor = self.colorMap[eleMapa]
                elif eleMapa.simbolo in self.colorMap:
                    cor = self.colorMap[eleMapa.simbolo]
                else:
                    cor = (0, 0, 0)

                pygame.draw.rect(self.pygameDisplay, cor, (j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize))  # posição
                pygame.draw.rect(self.pygameDisplay, (200, 200, 200), (j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize), 1)  # contorno do grid
