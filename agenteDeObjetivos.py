from agenteDeEstados import AgenteDeEstados

class AgenteDeObjetivos(AgenteDeEstados):
    def __init__(self, simbolo: str, pos: tuple[int, int]):
        super().__init__(simbolo, pos)

    def movimentacao(self, visao):
        self.guarda_caminho()
        self.ultima_posicao = (self.x, self.y)

        # Verifica se ainda há recursos na lista
        for recurso in list(self.locais_com_recurso):
            pos_recurso = recurso
            # Verifica se o recurso ainda está no ambiente visível
            for (x, y, elementoMapa) in visao:
                if (x, y) == pos_recurso and elementoMapa.terreno.value.valor > 0:
                    # Planeja movimento até o recurso
                    proxima_pos = self.irAte(pos_recurso)
                    if proxima_pos == pos_recurso:
                        self.estado = self.EstadosAgente.COLETANDO
                    return proxima_pos
            else:
                # Se o recurso não está mais visível, assume que foi coletado e remove da lista
                self.locais_com_recurso.discard(pos_recurso)

        # Se nenhum recurso disponível, age como AgenteDeEstados (exploração inteligente)
        return super().movimentacao(visao)


def explorar(self, ambiente):
    if self.estado == self.EstadosAgente.ANDANDO:
        visao = self.verAmbiente(ambiente)
        novaPos = self.movimentacao(visao)
        self.deslocarAgente(ambiente, novaPos)

    elif self.estado == self.EstadosAgente.COLETANDO:
        # Tenta coletar recurso da célula atual
        valor, tipo = ambiente.coletarRecurso(self.x, self.y)

        if valor > 0:
            self.carga = valor
            print(f"{self.simbolo} coletou um recurso!")
            self.estado = self.EstadosAgente.VOLTANDO_BASE

        elif valor == 0:
            print(f"{self.simbolo}: Recurso já foi coletado.")
            # Remove da lista de recursos conhecidos
            self.locais_com_recurso.discard((self.x, self.y))
            self.estado = self.EstadosAgente.ANDANDO

    elif self.estado == self.EstadosAgente.VOLTANDO_BASE:
        novaPos = self.irAte(ambiente.posBase)
        self.deslocarAgente(ambiente, novaPos)

        if novaPos == ambiente.posBase:
            print(f"{self.simbolo} entregou recurso na base.")
            self.pontuacao += self.carga
            self.carga = 0
            self.estado = self.EstadosAgente.ANDANDO
            # Atualiza lista de recursos, caso ainda tenha algum
            self.locais_com_recurso.discard((self.x, self.y))
