import time
import pygame

from view import View
from tipoTerreno import Tipo
from ambiente import Ambiente
from agenteReativoSimples import AgenteReativoSimples
from agenteDeEstados import AgenteDeEstados, AgenteBase
from agenteDeObjetivos import AgenteDeObjetivos
from agenteBDI import AgenteBDI

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

    def agentesExplorar(self):
        for a in self.agentes:
            a.explorar(self.ambiente)
        self.execucoes += 1

    def executar(self) -> bool:
        auto = self.automatico

        if self.ambiente.recursosRestantes <= 0:
            return False

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
        if auto:
            self.agentesExplorar()
        self.automatico = auto
        return True

    def tempoDeExecucao(self):
        print(f"{time.time() - self.tempoInicial:.2f} segundos")
    
    def numeroExecucoes(self):
        print(f"Números de Execuções: {self.execucoes} ")

if __name__ == "__main__":
    ambiente = Ambiente(3, 3)

    ambiente.preencherMapa(Tipo.METAL, 0)
    ambiente.preencherMapa(Tipo.CRISTAL, 0)
    ambiente.preencherMapa(Tipo.ESTRUTURA, 1)

    tela = View(ambiente.largura, ambiente.altura, 16)
            
    posBase = (ambiente.largura // 2, ambiente.altura // 2)
    ambiente.adicionarBase(posBase)

    agenteBDI = AgenteBDI(posBase[0], posBase[1])
    agentes_info = [
        #('A', AgenteReativoSimples, (34, 139, 34)), # Verde
        #('B', AgenteDeEstados, (139, 34, 34)),   #Marrom
        ('M', AgenteDeObjetivos, (128, 0, 128)), # Roxo
    ]
    #Adicionar múltiplos agentes
    # for _ in range(1):
    #      agentes_info.append(('M', AgenteDeEstados, (128, 0, 128)))
    
    agentes = []
    for simbolo, classe, cor in agentes_info:
        agente = classe(simbolo, posBase, agenteBDI)
        tela.adicionarElementoVisual(agente.simbolo, cor)
        ambiente.adicionarAgente(agente)
        agentes.append(agente)

    simulacao = Simulacao(ambiente, agentes, 5, False)

    clock = pygame.time.Clock()
    velocidade = 10 #Número médio de excuções por segundo
    rodando = True
    # True inicia a exploração dos agentes de forma automática
    # False começa de forma manual
    # Inputs
    # ENTER altera entre um desses modos
    # ESPACO Roda a exploração 1 vez quando está parado

    completo = False
    while rodando:
        rodando = simulacao.executar()
        tela.exibir(simulacao.completo, ambiente, agenteBDI)
        clock.tick(velocidade)  # Limita o loop para rodar a 30 frames por segundo

    simulacao.tempoDeExecucao()
    simulacao.numeroExecucoes()
    tela.fecharTela()