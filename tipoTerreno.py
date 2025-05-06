from enum import Enum

class Terreno():
    def __init__(self, simbolo:str, valor:int):
        self.simbolo = simbolo
        self.valor = valor
    
    def __str__(self):
        return self.simbolo
    
    def coletar(self) -> tuple[int, "Tipo"]:
        if self.valor > 0:
            valor = self.valor
            return (valor, Tipo.LIVRE)
        return (0, self)

class Estrutura(Terreno):
    def coletar(self, entidades):
        if (len(entidades) >= 2):
            return super().coletar()
        return 0

class Tipo(Enum):
    RIO = Terreno('~', -20)
    LIVRE = Terreno('.', 0)
    BASE = Terreno('@', 0)
    CRISTAL = Terreno('*', 10)
    METAL = Terreno('!', 20)
    ESTRUTURA = Terreno('#', 50)