import random
import pygame
from tipoTerreno import Tipo 
from ambiente import Ambiente
from agenteBase import AgenteBase

#parametros do ambiente
GRID_ROWS = 50
GRID_COLS = 50

#cores pygame
COLOR_MAP = {
    Tipo.LIVRE:     (255, 255, 255),       # branco
    Tipo.RIO:       (000, 255, 255),       # ciano
    Tipo.BASE:      (255, 255, 000),       # amarelo
    Tipo.CRISTAL:   (255, 000, 255),       # Roxo
    Tipo.METAL:     (111, 111, 111),       # cinza
    Tipo.ESTRUTURA: (255, 000, 000)        # vermelho
}

#parametros do ambiente - pygame
CELL_SIZE = 16  #pixels
WINDOW_WIDTH = GRID_COLS * CELL_SIZE
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE

def preencherMapa(ambiente, elemento, quantidade):
    count = 0
    while count < quantidade:
        i = random.randint(0, ambiente.largura - 1)
        j = random.randint(0, ambiente.altura - 1)
        if ambiente.mapa[i][j].terreno == Tipo.LIVRE:
            ambiente.mapa[i][j].posicionarElemento(elemento)
            count += 1

#pygame
def desenhar_grid(tela, ambiente):
    for i in range(len(ambiente.mapa)):
        for j in range(len(ambiente.mapa[0])):
            eleMapa = ambiente.mapa[i][j]
            terreno = eleMapa.terreno

            if terreno in COLOR_MAP:
                cor = COLOR_MAP[terreno]
            else:
                cor = (0, 0, 0)

            if eleMapa.entidade != []:
                cor = COLOR_MAP[str(eleMapa)]
            pygame.draw.rect(tela, cor, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)) #posicao
            pygame.draw.rect(tela, (200, 200, 200), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)  #contorno do grid


#criando ambiente
grid = Ambiente(GRID_ROWS, GRID_COLS)
agente = AgenteBase('A', GRID_ROWS//2, GRID_COLS//2)
grid.adicionarEntidade(agente.x, agente.y, agente)

# Adicionando um novo tipo de terreno ao enum Tipo
COLOR_MAP[agente.simbolo] = (34, 139, 34)  # verde floresta

grid.adicionarBase(GRID_ROWS//2, GRID_COLS//2)
preencherMapa(grid, Tipo.RIO, 30)
preencherMapa(grid, Tipo.CRISTAL, 20)
preencherMapa(grid, Tipo.METAL, 10)
preencherMapa(grid, Tipo.ESTRUTURA, 3)

#exibido a matriz
grid.printMapa()

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
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            agente.explorar(grid)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            agente.explorar(grid)

    tela.fill((0, 0, 0))
    desenhar_grid(tela, grid)
    pygame.display.flip()
    
    pygame.time.Clock().tick(30)  # Limita o FPS a 30
pygame.quit()
