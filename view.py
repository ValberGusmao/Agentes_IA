import pygame

from tipoTerreno import Tipo

class View():

    def __init__(self, largura, altura, cellSize):
        # Dimensões da janela
        self.cellSize = cellSize
        self.largura = largura
        self.altura = altura

        # Inicializar pygame
        pygame.init()
        self.pygameDisplay = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Planeta Desconhecido")

        # Posição inicial da câmera
        self.cameraX = 0
        self.cameraY = 0

        # Carregar sprites originais
        self.spriteMapOriginal = {
            Tipo.LIVRE: pygame.image.load("sprites/livre.png"),
            Tipo.BASE: pygame.image.load("sprites/base.png"),
            Tipo.CRISTAL: pygame.image.load("sprites/cristal.png"),
            Tipo.METAL: pygame.image.load("sprites/metal.png"),
            Tipo.ESTRUTURA: pygame.image.load("sprites/estrutura.png"),
        }

        # Criar uma cópia redimensionada dos sprites
        self.spriteMap = {}
        self.redimensionarSprites()

    def redimensionarSprites(self):
        """
        Redimensiona os sprites com base no tamanho atual das células,
        mantendo as proporções originais de cada sprite.
        """
        for key in self.spriteMapOriginal:
            sprite_original = self.spriteMapOriginal[key]
            largura_original, altura_original = sprite_original.get_size()

            # Calcular o fator de escala com base no tamanho da célula
            fator_escala = self.cellSize / 16  # Base de referência é 16x16
            nova_largura = int(largura_original * fator_escala)
            nova_altura = int(altura_original * fator_escala)

            # Redimensionar o sprite mantendo as proporções
            self.spriteMap[key] = pygame.transform.scale(sprite_original, (nova_largura, nova_altura))
        
    def ajustarZoom(self, fator):
        """
        Ajusta o zoom alterando o tamanho das células.

        Args:
            fator (float): Fator de zoom. Valores maiores que 1 aumentam o zoom, menores que 1 diminuem.
        """
        novoTamanho = self.cellSize + fator
        if 8 <= novoTamanho <= 64:  # Limita o tamanho das células entre 8 e 64 pixels
            self.cellSize = novoTamanho
            self.redimensionarSprites()

    def moverCamera(self, dx, dy, mapaLargura, mapaAltura):
        """
        Move a câmera em uma direção específica, garantindo que ela não saia dos limites do mapa.

        Args:
            dx (int): Deslocamento horizontal da câmera.
            dy (int): Deslocamento vertical da câmera.
            mapaLargura (int): Largura total do mapa em células.
            mapaAltura (int): Altura total do mapa em células.
        """
        # Atualiza a posição da câmera, garantindo que ela não ultrapasse os limites do mapa
        self.cameraX = max(0, min(self.cameraX + dx, mapaLargura - self.largura // self.cellSize))
        self.cameraY = max(0, min(self.cameraY + dy, mapaAltura - self.altura // self.cellSize))

    def exibir(self, completo: bool, ambiente, bdi):
        self.pygameDisplay.fill((0, 0, 0))
        self.preencherComSprite(self.spriteMapOriginal[Tipo.LIVRE], ambiente)

        if completo:
            self.desenhar_grid(ambiente)
        else:
            self.desenharApenasDescobertos(ambiente, bdi)

        self.desenharAgentes(ambiente)
        pygame.display.flip()

    def preencherComSprite(self, sprite, ambiente):
        # Carregar o sprite
        sprite = pygame.transform.scale(sprite, (self.cellSize, self.cellSize))  # Ajustar o tamanho do sprite
        altura = min(self.altura // self.cellSize + 1, ambiente.altura)
        largura = min(self.largura // self.cellSize + 1, ambiente.largura)

        # Preencher a tela com o sprite
        for y in range(altura):
            for x in range(largura):
                self.pygameDisplay.blit(sprite, (x * self.cellSize, y * self.cellSize))

    def adicionarElementoVisual(self, chave: str, spritePath: str):
        """
        Adiciona um novo sprite ao mapa de sprites.

        Args:
            chave (str): Chave para identificar o sprite.
            spritePath (str): Caminho para o arquivo de imagem do sprite.
        """
        spriteOriginal = pygame.image.load(spritePath)
        self.spriteMapOriginal[chave] = spriteOriginal
        self.spriteMap[chave] = pygame.transform.scale(spriteOriginal, (self.cellSize, self.cellSize))
    
    def desenharAgentes(self, ambiente):
        """
        Desenha os agentes no mapa, ajustando suas posições com base na câmera.

        Args:
            ambiente (Ambiente): O ambiente contendo os agentes.
        """
        for agente in ambiente.agentes:
            # Ajustar as coordenadas do agente com base na câmera
            x = (agente.x - self.cameraX) * self.cellSize
            y = (agente.y - self.cameraY) * self.cellSize

            # Verificar se o agente está dentro da área visível
            if 0 <= x < self.largura and 0 <= y < self.altura:
                if agente.simbolo in self.spriteMap:
                    sprite = self.spriteMap[agente.simbolo]
                else:
                    sprite = None

                if sprite:
                    # Ajustar o pivot para o canto inferior esquerdo
                    largura_sprite, altura_sprite = sprite.get_size()
                    pos_x = x
                    pos_y = y + self.cellSize - altura_sprite  # Ajusta para o canto inferior esquerdo
                    self.pygameDisplay.blit(sprite, (pos_x, pos_y))


    def desenharApenasDescobertos(self, ambiente, bdi):
        altura = min(self.altura // self.cellSize, ambiente.altura)
        largura = min(self.largura // self.cellSize, ambiente.largura)

        for i in range(altura):
            for j in range(largura):

                mapaX = self.cameraX + j
                mapaY = self.cameraY + i

                if mapaY < ambiente.altura and mapaX < ambiente.largura:
                    eleMapa = ambiente.mapa[mapaY][mapaX].getElemento()

                    if (j, i) in bdi.recursosConhecidos:
                        #Recursos
                        if eleMapa in self.spriteMap:
                            sprite = self.spriteMap[eleMapa]
                    #Base / BDI
                    elif (i, j) == (bdi.x, bdi.y):
                        sprite = self.spriteMap[eleMapa]
                    else:
                        sprite = None

                    if sprite:
                        # Ajustar o pivot para o canto inferior esquerdo
                        pos_x = j * self.cellSize
                        pos_y = (i + 1) * self.cellSize - sprite.get_size()[1]  # Ajusta para o canto inferior esquerdo
                        self.pygameDisplay.blit(sprite, (pos_x, pos_y))

    def desenhar_grid(self, ambiente):
        altura = min(self.altura // self.cellSize, ambiente.altura)
        largura = min(self.largura // self.cellSize, ambiente.largura)

        for i in range(altura):
            for j in range(largura):
                # Coordenadas no mapa, ajustadas pela câmera
                mapaX = self.cameraX + j
                mapaY = self.cameraY + i

                if mapaY < ambiente.altura and mapaX < ambiente.largura:
                    eleMapa = ambiente.mapa[mapaY][mapaX].getElemento()

                    sprite = None
                    if eleMapa in self.spriteMap:
                        if eleMapa != Tipo.LIVRE:
                            sprite = self.spriteMap[eleMapa]

                    if sprite:
                        # Ajustar o pivot para o canto inferior esquerdo
                        pos_x = j * self.cellSize
                        pos_y = (i + 1) * self.cellSize - sprite.get_size()[1]  # Ajusta para o canto inferior esquerdo
                        self.pygameDisplay.blit(sprite, (pos_x, pos_y))
    
    def fecharTela(self):
        pygame.quit()
