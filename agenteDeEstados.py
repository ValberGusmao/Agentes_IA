from agenteBase import AgenteBase, Carga

class AgenteDeEstados(AgenteBase):
    # Explora como o reativo simples, porem evita coordenadas ja visitadas por ele
    # Entao ele vai guardando o caminho dele ate encontrar um recurso
    # verifica se o local ja foi visitado
    # se nao verifica se tem recurso e faz a logica do reativo simples
    # Quando encontra um recurso ele deve continuar seguindo por caminhos aleatorios e salvando seu caminho mas deve voltar para a base (ainda nao fiz isso)
    # Volta para base: deve pegar caminho novo para descobrir mais caminhos, quando chegar na base deve atualizar sua lista com BDI
    # BDI deve remover da lista locais_com_recursos o local que os agentes pegaram um recurso
    def __init__(self, simbolo:str, pos:tuple[int, int], BDI):
        super().__init__(simbolo, pos, BDI)  
        self.locais_visitados = set()
        self.locais_com_recurso = set()
        self.ultima_posicao = None  # Armazena a última posição visitada
        self.guarda_caminho()  # guardando posicao inicial

    def guarda_caminho(self):
        self.locais_visitados.add((self.x, self.y))

    def guarda_local_recurso(self, x, y):
        self.locais_com_recurso.add((x, y))
       # print(f"\nRecursos conhecidos: {self.locais_com_recurso}")

    def movimentacao(self, recursos, visao):
        maior = 0
        opcoes = []

        # Guardamos a posição atual antes de nos movermos
        self.ultima_posicao = (self.x, self.y)
        self.guarda_caminho()
        
        lista = recursos
        if lista == []:
            lista = visao
            
        for (x, y, elementoMapa) in lista:
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
        
        else:
            # se nao houver caminho novo para seguir, segue qualquer um
            res = self.escolherAleatorio(opcoes)
            #  se todas já foram visitadas
            if res is None:
                todas_opcoes = []
                for (x, y, _) in visao:
                    if (self.x - x == 0 or self.y - y == 0):
                        if (x, y) != self.ultima_posicao:
                            todas_opcoes.append((x, y))
                
                res = self.escolherAleatorio(todas_opcoes)
            return res

    def verificarRecursos(self, visao) -> tuple[int, int, any]:
        recursos = super().verificarRecursos(visao)
        for r in recursos:
            self.guarda_local_recurso(r[0], r[1])
        return recursos

    def entrouNaBase(self, carga:Carga):
        super().entrouNaBase(carga)
        self.locais_com_recurso.update(self.BDI.atualizarCrencas(self.locais_com_recurso))