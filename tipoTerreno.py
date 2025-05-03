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
    BASE = Terreno('@', 0)
    CRISTAL = Terreno('*', 10)
    METAL = Terreno('!', 20)
    ESTRUTURA = Terreno('#', 50)