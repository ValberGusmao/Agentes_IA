from agenteBase import Carga
from elementoMapa import Tipo


class AgenteBDI():
    def __init__(self, x: int, y: int, tamX, tamY):
        self.x = x
        self.y = y
        self.tamX = tamX
        self.tamY = tamY
        self.recursosConhecidos: set[tuple[int, int]] = set()
        self.recursosColetado: set[tuple[int, int]] = set()
        self.agentesCooperativos: list = []
        self.todoMapa: set[tuple[int, int]] = set()
        self.preencherMapa()
        
    def preencherMapa(self):
        for i in range(self.tamX):
            for j in range(self.tamY):
                self.todoMapa.add((i, j))

    def depositarCarga(self, carga: Carga):
        pos = (carga.x, carga.y)
        self.recursosColetado.add(pos)

    def atualizarCrencas(self, recursos: list):
        novos_conhecidos = set()
        for r in recursos:
            if r not in self.recursosColetado:
                novos_conhecidos.add(r)

        # By Copilor
        self.recursosConhecidos.update(novos_conhecidos)
        self.recursosConhecidos.difference_update(self.recursosColetado)
        return self.recursosConhecidos

    # Para o agente de Objetivos
    def definirObjetivo(self) -> tuple[int, int]:
        if (len(self.recursosConhecidos) > 0):
            objetivo = list(self.recursosConhecidos)[0]
            return objetivo

    def agenteSaiuDaBase(self):
        pass

    def receberMensagemBDI(self, mensagem):
        # print("BDI: Recebi a mensagem sobre a posicao da estrutura.")
        if mensagem['tipo'] == Tipo.ESTRUTURA:
            # print(f"Estrutura em {mensagem['posicao']}")
            # aqui adiciono o local da estrutura na lista de recurso conhecidos
            self.recursosConhecidos.add(mensagem['posicao'])
            # for a in self.agentesCooperativos:
            #     a.receberMensagemCoop(self.enviarMensagemBDI())

    # def enviarMensagemBDI(self):
    #     print("enviando mensagem de estrutura")
    #     # enviando lista de estruturas
    #     return self.recursosConhecidos
