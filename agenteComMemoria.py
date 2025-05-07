from agenteBase import AgenteBase


class AgenteComMemoria(AgenteBase):

    # Explora como o reativo simples, porem evita coordenadas ja visitadas por ele
    # Entao ele vai guardando o caminho dele ate encontrar um recurso
    # verifica se o local ja foi visitado
    # se nao verifica se tem recurso e faz a logica do reativo simples
    # Quando encontra um recurso ele deve continuar seguindo por caminhos aleatorios e salvando seu caminho mas deve voltar para  a base (ainda nao fiz isso)

    def __init__(self, simbolo, x, y):
        super().__init__(simbolo, x, y)
        self.locais_visitados = set()
        self.guarda_caminho  # guardando posicao inicial

    def guarda_caminho(self):
        self.locais_visitados.add((self.x, self.y))

    def movimentacao(self, visao):
        locais_nao_visitados = []
        for (x, y, elemento) in visao:
            if (x, y) not in self.locais_visitados:  # significa quqe sao locais que é preferivel visitar
                locais_nao_visitados.append((x, y, elemento))

        maior = 0
        opcoes = []
        # vai olhar apenas para locais que nao foram visitados
        for (x, y, elementoMapa) in locais_nao_visitados:
            valor = elementoMapa.terreno.value.valor
            if valor > maior:
                maior = valor
                pos = (x, y)
            elif (self.x - x == 0 or self.y - y == 0):
                opcoes.append((x, y))

        if maior != 0:
            # O recurso tá na diagonal. O agente tem que escolher entre duas opções em linha reta
            if self.x - pos[0] != 0 and self.y - pos[1] != 0:
                opcoes = [(pos[0], self.y), (self.x, pos[1])]
                self.guarda_caminho()
                return self.escolherAleatorio(opcoes)
            else:
                self.estado = self.EstadosAgente.COLETANDO
                self.guarda_caminho()
                return pos

        else:  # se nao houver caminho novo para seguir, segue qualquer um
            res = self.escolherAleatorio(opcoes) if opcoes else None
            if res is not None:
                self.guarda_caminho()
                return (res[0], res[1])
            else:
                opcoes = []
                for (x, y, elemento) in visao:
                    opcoes.append((x, y))
                res = self.escolherAleatorio(opcoes)
                self.guarda_caminho
                return res
