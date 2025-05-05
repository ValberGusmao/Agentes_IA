from tipoTerreno import *
    
class ElementoMapa():
    def __init__(self, terreno:Tipo = Tipo.LIVRE):
        self.terreno = terreno
        self.entidades = []

    def __str__(self):
        if self.entidades:
            return str(self.entidades[0])
        return str(self.terreno.value)
    
    def getElemento(self):
        if self.entidades:
            return self.entidades[0]
        return self.terreno

    def adicionarEntidade(self, entidade):
        if entidade not in self.entidades:
            self.entidades.append(entidade)
    def posicionarElemento(self, elemento):
        self.terreno = elemento

    def coletarRecurso(self):
        #  estrutura precisa de dois ou mais agentes
        if self.terreno == Tipo.ESTRUTURA:
            if len(self.entidades) >= 2:
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

    def moverEntidade(self, ent, proximaPosicao: 'ElementoMapa'):
        proximaPosicao.entidades.append(ent)
        # if ent in self.entidades:
        self.entidades.remove(ent)