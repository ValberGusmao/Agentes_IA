import random
from ambiente import Ambiente
from agenteBase import AgenteBase
from tipoTerreno import Tipo

if __name__ == "__main__":
    mapa = Ambiente(17, 17)
    agenteSimples = AgenteBase('A', 8, 8)

    mapa.adicionarEntidade(8,8, agenteSimples)

    for _ in range (30):
        x, y = random.randint(0, mapa.largura - 1), random.randint(0, mapa.altura - 1)
        mapa.adicionarRecurso(x, y, Tipo.CRISTAL)

    for _ in range(20):
        agenteSimples.explorar(mapa)
        print()
        mapa.printMapa()
