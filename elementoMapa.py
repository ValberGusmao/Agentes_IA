from tipoTerreno import *
    
class ElementoMapa():
    def __init__(self, terreno:Tipo = Tipo.LIVRE):
        self.terreno = terreno
        self.agentes = []
    
    def adicionarAgente(self, entidade):
        if entidade not in self.agentes:
            self.agentes.append(entidade)

    def posicionarElemento(self, elemento: Tipo):
        self.terreno = elemento

    def moverAgente(self, ent, proximaPosicao: 'ElementoMapa'):
        proximaPosicao.agentes.append(ent)
        # if ent in self.entidades: Ajuda a identificar erros isso não esta sendo verificado
        self.agentes.remove(ent)

    def coletarRecurso(self) -> int:
        #  estrutura precisa de dois ou mais agentes
        if self.terreno == Tipo.ESTRUTURA:
            if len(self.agentes) >= 2:
                valor = self.terreno.value.coletar()
                if valor[0] > 0:
                    self.terreno = valor[1]  # limpa o terreno
                return valor[0]
            else:
                #estrutura encontrada mas nao ha agentes suficientes
                return -2  #estrutura requer 2 agentes
        else:
            # pode coletar sozinho
            valor = self.terreno.value.coletar()
            if valor[0] > 0:
                self.terreno = valor[1]
            return valor[0]

    def getElemento(self) -> "ElementoMapa":
        if self.agentes:
            return self.agentes[0]
        return self.terreno

    def __str__(self):
        if self.agentes:
            return str(self.agentes[0])
        return str(self.terreno.value)