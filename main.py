from ambiente import Ambiente
from agenteBase import AgenteBase

if __name__ == "__main__":
    mapa = Ambiente(17, 17)
    agenteSimples = AgenteBase(8, 8)

    mapa.adicionarEntidade(8,8, agenteSimples)

    for _ in range(20):
        agenteSimples.explorar(mapa)

    mapa.printMapa()