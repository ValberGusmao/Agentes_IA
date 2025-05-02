'''class Cenario:
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
'''

import random
import pygame

#constantes do ambiente
TERRAIN_FREE = '.'
OBSTACLE = '#'
BASE = 'B'
CRYSTAL = 'C'
METAL = 'M'
STRUCTURE = 'S'

#parametros do ambiente
GRID_ROWS = 10
GRID_COLS = 10
NUM_OBSTACLES = 15
NUM_CRYSTALS = 5
NUM_METALS = 4
NUM_STRUCTURES = 2

#cores pygame
COLOR_MAP = {
    TERRAIN_FREE: (255, 255, 255),    # branco
    OBSTACLE: (80, 80, 80),           # cinza escuro
    BASE: (0, 0, 255),                # azul
    CRYSTAL: (0, 255, 0),             # verde
    METAL: (255, 255, 0),             # amarelo
    STRUCTURE: (255, 0, 0)            # vermelho
}

#parametros do ambiente - pygame
CELL_SIZE = 50  #pixels
WINDOW_WIDTH = GRID_COLS * CELL_SIZE
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE


def criar_grid(rows, cols):
    grid = []
    for _ in range(rows):
        linha = []
        for _ in range(cols):
            linha.append(TERRAIN_FREE)
        grid.append(linha)
    return grid


def posicionar_base(grid):
    centro_linha = len(grid) // 2
    centro_coluna = len(grid[0]) // 2
    grid[centro_linha][centro_coluna] = BASE
    return (centro_linha, centro_coluna) #retorna os indices


def posicionar_elementos(grid, elemento, quantidade):
    linhas = len(grid)
    colunas = len(grid[0])
    count = 0
    while count < quantidade:
        i = random.randint(0, linhas - 1)
        j = random.randint(0, colunas - 1)
        if grid[i][j] == TERRAIN_FREE:
            grid[i][j] = elemento
            count += 1


def exibir_grid(grid):
    for linha in grid:
        print(' '.join(linha))
    print()


#pygame
def desenhar_grid(tela, grid):
    for i, linha in enumerate(grid):
        for j, celula in enumerate(linha):
            if celula in COLOR_MAP:
                cor = COLOR_MAP[celula]
            else:
                cor = (0, 0, 0)  # cor preta padrão

            pygame.draw.rect(tela, cor, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)) #posicao
            pygame.draw.rect(tela, (200, 200, 200), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)  #contorno do grid


#criando ambiente
grid = criar_grid(GRID_ROWS, GRID_COLS)
posicionar_base(grid)
posicionar_elementos(grid, OBSTACLE, NUM_OBSTACLES)
posicionar_elementos(grid, CRYSTAL, NUM_CRYSTALS)
posicionar_elementos(grid, METAL, NUM_METALS)
posicionar_elementos(grid, STRUCTURE, NUM_STRUCTURES)

#exibido a matriz
exibir_grid(grid)

#iniciar pygame
pygame.init()
tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Planeta Desconhecido")

#loop de controle
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))
    desenhar_grid(tela, grid)
    pygame.display.flip()
    
    pygame.time.Clock().tick(30)  # Limita o FPS a 30
pygame.quit()


