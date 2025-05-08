from agenteDeEstados import AgenteDeEstados

class AgenteDeObjetivos(AgenteDeEstados):
    def __init__(self, simbolo: str, pos: tuple[int, int], bdi):
        super().__init__(simbolo, pos, bdi)
        self.objetivo:tuple[int, int] = None

    def movimentacao(self, visao):
        if self.objetivo != None:
            res = self.irAte(self.objetivo)
            if res == (self.x, self.y):
                self.estado = self.EstadosAgente.COLETANDO
            return res

        else:
            return super().movimentacao(visao)
    
    def entrouNaBase(self, carga):
        super().entrouNaBase(carga)
        self.objetivo = self.BDI.definirObjetivo()

    def coletar(self, ambiente):
        val =  super().coletar(ambiente)
        if val == 0:
            self.estado = self.EstadosAgente.VOLTANDO_BASE
        return val