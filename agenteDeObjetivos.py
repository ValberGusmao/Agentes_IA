from agenteDeEstados import AgenteDeEstados
from elementoMapa import Tipo

class AgenteDeObjetivos(AgenteDeEstados):
    def __init__(self, simbolo: str, pos: tuple[int, int], bdi):
        super().__init__(simbolo, pos, bdi)
        self.objetivo:tuple[int, int] = None

    def movimentacao(self, recursos, visao) -> tuple[int, int]:
        if self.objetivo != None:
            res = self.irAte(self.objetivo)
            if res == (self.x, self.y):
                self.estado = self.EstadosAgente.COLETANDO
            return res

        else:
            return super().movimentacao(recursos, visao)
    
    def entrouNaBase(self, carga):
        super().entrouNaBase(carga)
        self.objetivo = self.BDI.definirObjetivo()

    def coletar(self, ambiente):
        val, tipo =  super().coletar(ambiente)
        if val == 0 and tipo != Tipo.ESTRUTURA:
            self.estado = self.EstadosAgente.VOLTANDO_BASE
        return val