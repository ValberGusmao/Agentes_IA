import time
import pygame

from view import View
from tipoTerreno import Tipo
from ambiente import Ambiente
from agenteDeObjetivos import AgenteDeObjetivos
from agenteBDI import AgenteBDI


class Simulacao:
    def __init__(self, ambiente: Ambiente, agentes: list, tempoLimite: int, automatico: bool = True):
        self.tempoLimite = tempoLimite
        self.automatico = automatico
        self.ambiente = ambiente
        self.agentes = agentes
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
    ambiente = Ambiente(25, 25)

    # Definindo as posições dos recursos manualmente
    recursos = [
        (5, 5, Tipo.CRISTAL),
        (8, 8, Tipo.METAL),
        (12, 12, Tipo.CRISTAL),
        (20, 20, Tipo.METAL),
        (15, 15, Tipo.ESTRUTURA)
    ]

    # Adicionando recursos ao mapa
    for x, y, recurso in recursos:
        ambiente.adicionarRecurso(x, y, recurso)

    # Criando a base no meio do mapa
    posBase = (ambiente.largura // 2, ambiente.altura // 2)
    ambiente.adicionarBase(posBase)

    bdi = AgenteBDI()
    # Adicionando o Agente de Objetivos
    agente = AgenteDeObjetivos("M", posBase, bdi)  # Agente de Objetivos na posição da base
    ambiente.adicionarAgente(agente)

    tela = View(ambiente.largura, ambiente.altura, 16)

    # Iniciando a simulação
    simulacao = Simulacao(ambiente, [agente], 5)

    clock = pygame.time.Clock()
    velocidade = 10  # Número médio de execuções por segundo
    rodando = True

    while rodando:
        rodando = simulacao.executar()
        tela.exibir(ambiente, bdi)
        clock.tick(velocidade)

    simulacao.tempoDeExecucao()
    simulacao.numeroExecucoes()
    tela.fecharTela()
