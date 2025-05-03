from enum import Enum

class Terreno():
    def __init__(self, simbolo:str, valor):
        self.simbolo = simbolo
        self.valor = valor
    
    def __str__(self):
        return self.simbolo

class Tipo(Enum):
    RIO = Terreno('~', -20)
    LIVRE = Terreno('.', 0)
    CRISTAL = Terreno('*', 10)
    METAL = Terreno('#', 20)
    ESTRUTURA = Terreno('@', 50)
    
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

    def adicionarRecurso(self, recurso):
        self.terreno = recurso

    def coletarRecurso(self, entidades):
        self.recurso = None

    def moverEntidade(self, ent, proximaPosicao: 'ElementoMapa'):        
        proximaPosicao.entidade.append(ent)
        self.entidade.remove(ent)