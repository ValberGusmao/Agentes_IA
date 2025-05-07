import time
import pygame

from view import View
from tipoTerreno import Tipo
from ambiente import Ambiente
from agenteReativoSimples import AgenteReativoSimples, AgenteBase
from agenteComMemoria import AgenteComMemoria, AgenteBase

# Responsável por unir todos os elementos


class Simulacao:
    def __init__(self, tela: View, ambiente: Ambiente, agentes: list[AgenteBase], tempoLimite: int):
        self.tempoLimite = tempoLimite
        self.tela = tela
        self.ambiente = ambiente
        self.agentes = agentes

    def agentesExplorar(self):
        for a in self.agentes:
            a.explorar(self.ambiente)

    def executar(self, automatico: bool = True):
        rodando = True
        automatico = automatico
        tempoInicial = time.time()

        for a in self.agentes:
            ambiente.adicionarAgente(a)

        while rodando:
            tempoPassado = time.time() - tempoInicial
            tempoRestante = int(self.tempoLimite - tempoPassado)

            if tempoRestante < 0:
                print("Tempo limite atingido. Encerrando o programa.")
                tempoRestante = 0
                break

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:  # ENTER alterna entre manual e automático
                        automatico = not automatico
                    elif evento.key == pygame.K_SPACE and not automatico:  # SPACE executa explorar uma vez no modo manual
                        self.agentesExplorar()

            if automatico:
                self.agentesExplorar()

            tela.exibir(self.ambiente, tempoRestante)

        tela.fecharTela()


if __name__ == "__main__":
    ambiente = Ambiente(6, 6)
    tela = View(ambiente.largura, ambiente.altura, 48)

    meioX, meioY = ambiente.largura // 2, ambiente.altura // 2

    agente = AgenteReativoSimples('A', meioX, meioY)
    agenteB = AgenteReativoSimples('B', meioX, meioY)
    agenteMemoria = AgenteComMemoria('M', meioX, meioY)

    ambiente.adicionarBase(meioX, meioY)

    tela.adicionarElementoVisual(agente.simbolo, (34, 139, 34))
    tela.adicionarElementoVisual(agenteB.simbolo, (139, 34, 34))
    tela.adicionarElementoVisual(agenteMemoria.simbolo,(128, 0, 128))

    # ambiente.preencherMapa(Tipo.RIO, 0)
    ambiente.preencherMapa(Tipo.METAL, 2)
    ambiente.preencherMapa(Tipo.CRISTAL, 15)
    ambiente.preencherMapa(Tipo.ESTRUTURA, 1)

    simulacao = Simulacao(tela, ambiente, [agente, agenteB,agenteMemoria], 30)

    # True inicia a exploração dos agentes de forma automática
    # False começa de forma manual
    # Inputs
    # ENTER altera entre um desses modos
    # ESPACO Roda a exploração 1 vez quando está parado
    simulacao.executar(True)
