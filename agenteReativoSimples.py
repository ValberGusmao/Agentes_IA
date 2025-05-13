from agenteBase import AgenteBase, Tipo

class AgenteReativoSimples(AgenteBase):
    def movimentacao(self, recursos, visao) -> tuple[int, int]:
        maior = 0
        opcoes = []

        lista = recursos
        if lista == []:
            lista = visao
            
        for (x, y, elementoMapa) in lista:
            valor = elementoMapa.terreno.value.valor
            if valor > maior:
                maior = valor
                pos = (x, y)
            elif (self.x - x == 0 or self.y - y == 0):
                opcoes.append((x, y))
        
        if maior != 0:
            #O recurso tá na diagonal. O agente tem que escolher entre duas opções em linha reta
            res = self.quebrarDiagonal((self.x, self.y),pos)
            if res == pos:
                self.estado = self.EstadosAgente.COLETANDO
            return res
        
        else:
            res = self.escolherAleatorio(opcoes)
            return (res[0], res[1])

    def verAmbiente(self, ambiente):
        res =  super().verAmbiente(ambiente)
        for x, y, elemento in res:
            if elemento.terreno == Tipo.ESTRUTURA:
                res.remove((x, y, elemento))
        return res
