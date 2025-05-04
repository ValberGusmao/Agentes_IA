from agenteBase import AgenteBase

class AgenteReativoSimples(AgenteBase):
    def movimentacao(self, visao):
        maior = 0
        opcoes = []
        for (x, y, elementoMapa) in visao:
            valor = elementoMapa.terreno.value.valor
            if valor > maior:
                maior = valor
                pos = (x, y)
            elif (self.x - x == 0 or self.y - y ==0):
                opcoes.append((x, y))
        
        if maior != 0:
            #O recurso tá na diagonal. O agente tem que escolher entre duas opções em linha reta
            if self.x - pos[0] != 0 and self.y - pos[1] != 0:
                opcoes = [(pos[0], self.y), (self.x, pos[1])]
                return self.escolherAleatorio(opcoes)
            else:
                self.estado = self.EstadosAgente.COLETANDO
                return pos
        else:
            res = self.escolherAleatorio(opcoes)
            return (res[0], res[1])
    