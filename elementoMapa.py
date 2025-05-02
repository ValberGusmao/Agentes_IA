class ElementoMapa():
    def __init__(self, valor:int, simbolo:str):
        self.valor = valor
        self.simbolo = simbolo

    def __str__(self):
        return self.simbolo