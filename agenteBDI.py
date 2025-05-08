from agenteBase import Carga

class AgenteBDI():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.recursosConhecidos:set[tuple[int, int]] = set()
        self.recursosColetado:set[tuple[int, int]] = set()
        
    def depositarCarga(self, carga:Carga):
        pos = (carga.x, carga.y)
        self.recursosColetado.add(pos)

    def atualizarCrencas(self, recursos:list):
        novos_conhecidos = set()
        for r in recursos:
            if r not in self.recursosColetado:
                novos_conhecidos.add(r)
        
        #By Copilor
        self.recursosConhecidos.update(novos_conhecidos)
        self.recursosConhecidos.difference_update(self.recursosColetado)
        return self.recursosConhecidos

    # Para o agente de Objetivos
    def definirObjetivo(self) -> tuple[int, int]:
        objetivo = None
        min_distance = float('inf')
        
        for recurso in self.recursosConhecidos:
            distance = abs(self.x - recurso[0]) + abs(self.y - recurso[1])
            if distance < min_distance:
                min_distance = distance
                objetivo = recurso
                
        return objetivo

    def agenteSaiuDaBase(self):
        pass