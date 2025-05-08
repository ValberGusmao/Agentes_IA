from agenteBase import Carga

class AgenteBDI():
    def __init__(self):
        self.recursosConhecidos:set[tuple[int, int]] = set()
        
    def depositarCarga(self, carga:Carga):
        pos = (carga.x, carga.y)
        if pos in self.recursosConhecidos:
            self.recursosConhecidos.remove(pos)

    def atualizarCrencas(self, recursos:list):
        for r in recursos:
            self.recursosConhecidos.add(r)
        return self.recursosConhecidos

    # Para o agente de Objetivos
    def definirObjetivo(self) -> tuple[int, int]:
        objetivo = None
        min_distance = float('inf')
        
        for recurso in self.recursosConhecidos:
            distance = abs(self.x - recurso[0]) + abs(self.Y - recurso[1])
            if distance < min_distance:
                min_distance = distance
                objetivo = recurso
                
        return objetivo

    def agenteSaiuDaBase(self):
        pass