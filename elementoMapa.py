from tipoTerreno import *
    
class ElementoMapa():
    def __init__(self, terreno:Tipo = Tipo.LIVRE):
        self.terreno = terreno
        self.entidade = []

    def __str__(self):
        if self.entidade:
            return str(self.entidade[0])
        return str(self.terreno.value)
    
    def adicionarEntidade(self, entidade):
        self.entidade.append(entidade)

    def posicionarElemento(self, elemento):
        self.terreno = elemento

    def coletarRecurso(self):
        valor = self.terreno.value.valor
        if valor > 0:
            self.terreno = Tipo.LIVRE
            return valor
        return 0
    
    def moverEntidade(self, ent, proximaPosicao: 'ElementoMapa'):        
        proximaPosicao.entidade.append(ent)
        self.entidade.remove(ent)