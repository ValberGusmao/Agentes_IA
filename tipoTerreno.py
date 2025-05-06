from enum import Enum

class Terreno():
    def __init__(self, simbolo:str, valor:int):
        self.simbolo = simbolo
        self.valor = valor
    
    def __str__(self):
        return self.simbolo

class Tipo(Enum):
    RIO = Terreno('~', -20)
    LIVRE = Terreno('.', 0)
    BASE = Terreno('@', 0)
    CRISTAL = Terreno('*', 10)
    METAL = Terreno('!', 20)
    ESTRUTURA = Terreno('#', 50)
    #O terreno é uma estrutura-pre-coletada quando dois agentes estão nela,
    #e o primeiro já pegou seu recurso.
    #Uma estrutura não é removida direto do mapa, mas uma pre coletada sim
    ESTRUTURA_PRE_COLETADA = Terreno('#', 50)