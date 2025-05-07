from agenteBase import AgenteBase
from tipoTerreno import Tipo


class AgenteComMemoria(AgenteBase):
    # Explora como o reativo simples, porem evita coordenadas ja visitadas por ele
    # Entao ele vai guardando o caminho dele ate encontrar um recurso
    # verifica se o local ja foi visitado
    # se nao verifica se tem recurso e faz a logica do reativo simples
    # Quando encontra um recurso ele deve continuar seguindo por caminhos aleatorios e salvando seu caminho mas deve voltar para a base (ainda nao fiz isso)
    # Volta para base: deve pegar caminho novo para descobrir mais caminhos, quando chegar na base deve atualizar sua lista com BDI
    # BDI deve remover da lista locais_com_recursos o local que os agentes pegaram um recurso
    def __init__(self, simbolo, x, y):
        super().__init__(simbolo, x, y)
        self.locais_visitados = set()
        self.locais_com_recurso = set()
        self.ultima_posicao = None  # Armazena a última posição visitada
        self.guarda_caminho()  # guardando posicao inicial

    def guarda_caminho(self):
        self.locais_visitados.add((self.x, self.y))

    def guarda_local_recurso(self, x, y):
        self.locais_com_recurso.add((x, y))
        print(f"\nRecursos conhecidos: {self.locais_com_recurso}")

    def movimentacao(self, visao):
        maior = 0
        opcoes = []

        # Guardamos a posição atual antes de nos movermos
        self.ultima_posicao = (self.x, self.y)
        self.guarda_caminho()

        # vai olhar apenas para locais que nao foram visitados
        for (x, y, elementoMapa) in visao:
            terreno = elementoMapa.terreno
            valor = terreno.value.valor

            # para guardar o local do recurso em um conjunto assim que ve
            if terreno in {Tipo.CRISTAL, Tipo.METAL, Tipo.ESTRUTURA}:
                self.guarda_local_recurso(x, y)
                print(f"\nRecursos conhecidos: {self.locais_com_recurso}")

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
        else:
            # se nao houver caminho novo para seguir, segue qualquer um
            res = None
            if opcoes:
                res = self.escolherAleatorio(opcoes)

            #  se todas já foram visitadas
            if res is None:
                # todas as opções possíveis
                todas_opcoes = []
                for (x, y, _) in visao:
                    # nao inclui a ultima posicao
                    if (x, y) != self.ultima_posicao:
                        todas_opcoes.append((x, y))

                if todas_opcoes:
                    res = self.escolherAleatorio(todas_opcoes)
                else:
                    for (x, y, _) in visao:
                        todas_opcoes.append((x, y))
                    res = self.escolherAleatorio(todas_opcoes)

            return res
