import time
import pygame

from view import View
from tipoTerreno import Tipo
from ambiente import Ambiente
from agenteReativoSimples import AgenteReativoSimples
from agenteDeEstados import AgenteDeEstados, AgenteBase
from agenteDeObjetivos import AgenteDeObjetivos
from agenteBDI import AgenteBDI
from agenteCooperativo import AgenteCooperativo

# Responsável por unir todos os elementos

class Simulacao:
    def __init__(self, ambiente: Ambiente, agentes: list[AgenteBase], tempoLimite: int, automatico: bool = True):
        self.tempoLimite = tempoLimite
        self.automatico = automatico
        self.ambiente = ambiente
        self.agentes = agentes
        self.completo = False

        self.tempoInicial = time.time()
        self.execucoes = 0

    def agentesAvaliar(self):
        print("------------------------------------------------------------------------")
        simulacao.tempoDeExecucao()
        simulacao.numeroExecucoes()

        #Ordenar por maior pontuação
        self.agentes.sort(key=lambda agente: agente.pontuacao, reverse=True)
        for a in self.agentes:
            a.printMetricas()
        quant = ambiente.recursosRestantes
        if quant > 0:
            print(f"Ainda faltam {quant} recursos para serem coletados")
        else:
            print("Todos os recursos foram coletados")
        print("------------------------------------------------------------------------")

    def agentesExplorar(self):
        for a in self.agentes:
            a.explorar(self.ambiente)
        self.execucoes += 1

    def executar(self) -> bool:
        auto = self.automatico

        if self.ambiente.recursosRestantes <= 0:
            contiuar = False
            for a in agentes:
                if a.estado.value == 3:
                    contiuar = True
                    break
            if not contiuar:
                return contiuar

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # ENTER alterna entre manual e automático
                    auto = not auto
                if evento.key == pygame.K_ESCAPE:
                    self.completo = not self.completo  # ESC fecha o programa
                if evento.key == pygame.K_SPACE and not auto:  # SPACE executa explorar uma vez no modo manual
                    self.agentesExplorar()
                if evento.key == pygame.K_PLUS or evento.key == pygame.K_EQUALS:  # Tecla '+'
                    tela.ajustarZoom(8)  # Aumenta o zoom em 10%
                elif evento.key == pygame.K_MINUS:  # Tecla '-'
                    tela.ajustarZoom(-8)  # Diminui o zoom em 10%
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            tela.moverCamera(0, -1, ambiente.largura, ambiente.altura)
        if keys[pygame.K_DOWN]:
            tela.moverCamera(0, 1, ambiente.largura, ambiente.altura)
        if keys[pygame.K_LEFT]:
            tela.moverCamera(-1, 0, ambiente.largura, ambiente.altura)
        if keys[pygame.K_RIGHT]:
            tela.moverCamera(1, 0, ambiente.largura, ambiente.altura)

        if auto:
            self.agentesExplorar()
        self.automatico = auto
        return True

    def tempoDeExecucao(self):
        print(f"{time.time() - self.tempoInicial:.2f} segundos")
    
    def numeroExecucoes(self):
        print(f"Números de Execuções: {self.execucoes} ")

if __name__ == "__main__":
    #ambiente = Ambiente(96, 170)
    ambiente = Ambiente(25, 25)

    tela = View(800, 800, 32)
            
    posBase = (ambiente.largura // 2, ambiente.altura // 2)
    ambiente.adicionarBase(posBase)

    #Preencher deve vir depois de botar base, senão elas vai ficar em cima de um recurso.
    #Esse recurso vai deixar de exisitr, mas o ambiente ainda vai contabilizar
    ambiente.preencherMapa(Tipo.METAL, 20)
    ambiente.preencherMapa(Tipo.CRISTAL, 50)
    ambiente.preencherMapa(Tipo.ESTRUTURA, 5)

    agenteBDI = AgenteBDI(posBase[0], posBase[1])
    agentes_info = [
        ('A', AgenteReativoSimples, "sprites/reativoSimples.png"),  
        ('B', AgenteDeEstados, "sprites/estados.png"),       
        ('M', AgenteDeObjetivos, "sprites/objetivos.png"),    
        ('C', AgenteCooperativo, "sprites/cooperativo.png"),
    ]
    # Adicionar múltiplos agentes
    # for _ in range(1):
    #       agentes_info.append(('M', AgenteDeEstados, "sprites/reativoSimples.png"))
    
    agentes = []
    for simbolo, classe, sprite_path in agentes_info:
        agente = classe(simbolo, posBase, agenteBDI)
        tela.adicionarElementoVisual(agente.simbolo, sprite_path)
        ambiente.adicionarAgente(agente)
        agentes.append(agente)

    simulacao = Simulacao(ambiente, agentes, 5, True)

    clock = pygame.time.Clock()
    velocidade = 10  # Número médio de execuções por segundo
    rodando = True
    # True inicia a exploração dos agentes de forma automática
    # False começa de forma manual
    # Inputs
    # ENTER altera entre um desses modos
    # ESPACO Roda a exploração 1 vez quando está parado

    print(ambiente.recursosRestantes)
    completo = True
    simulacao.completo = completo
    while rodando:
        rodando = simulacao.executar()
        tela.exibir(simulacao.completo, ambiente, agenteBDI)
        clock.tick()  # Limita o loop para rodar a 30 frames por segundo

    simulacao.agentesAvaliar()
    tela.fecharTela()