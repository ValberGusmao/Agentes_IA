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

# def explorar(self, ambiente):
#     if self.estado == self.EstadosAgente.ANDANDO:
#         visao = self.verAmbiente(ambiente)
#         novaPos = self.movimentacao(visao)
#         self.deslocarAgente(ambiente, novaPos)

#     elif self.estado == self.EstadosAgente.COLETANDO:
#         # Tenta coletar recurso da célula atual
#         valor, tipo = ambiente.coletarRecurso(self.x, self.y)

#         if valor > 0:
#             self.carga = valor
#             print(f"{self.simbolo} coletou um recurso!")
#             self.estado = self.EstadosAgente.VOLTANDO_BASE

#         elif valor == 0:
#             print(f"{self.simbolo}: Recurso já foi coletado.")
#             # Remove da lista de recursos conhecidos
#             self.locais_com_recurso.discard((self.x, self.y))
#             self.estado = self.EstadosAgente.ANDANDO

#     elif self.estado == self.EstadosAgente.VOLTANDO_BASE:
#         novaPos = self.irAte(ambiente.posBase)
#         self.deslocarAgente(ambiente, novaPos)

#         if novaPos == ambiente.posBase:
#             print(f"{self.simbolo} entregou recurso na base.")
#             self.pontuacao += self.carga
#             self.carga = 0
#             self.estado = self.EstadosAgente.ANDANDO
#             # Atualiza lista de recursos, caso ainda tenha algum
#             self.locais_com_recurso.discard((self.x, self.y))
