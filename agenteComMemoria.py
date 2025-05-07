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
        self.guarda_caminho()  # guardando posicao inicial

    def guarda_caminho(self):
        self.locais_visitados.add((self.x, self.y))

    def movimentacao(self, visao):
        maior = 0
        opcoes = []

        self.guarda_caminho()

        # vai olhar apenas para locais que nao foram visitados
        for (x, y, elementoMapa) in visao:
            valor = elementoMapa.terreno.value.valor
            if valor > maior:
                maior = valor
                pos = (x, y)
            elif (x, y) not in self.locais_visitados:
                if (self.x - x == 0 or self.y - y == 0):
                    opcoes.append((x, y))
        
        if maior != 0:
            # O recurso tá na diagonal. O agente tem que escolher entre duas opções em linha reta
            res = self.quebrarDiagonal((self.x, self.y), pos)
            if res == pos:
                self.estado = self.EstadosAgente.COLETANDO
            return res

        else:  # se nao houver caminho novo para seguir, segue qualquer um
            res = self.escolherAleatorio(opcoes)
            if res == None:
                res = self.escolherAleatorio(visao)
            return (res[0], res[1])