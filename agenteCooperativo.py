from agenteDeObjetivos import AgenteDeObjetivos
import math
# quando o cooperativo pisa na base ele deve receber a lista de objetivos, no entanto ele precisa fazer um calculo para ver qual o objetivo 
# mais valioso e nao apenas seguir no mais proximo

class AgenteCooperativo(AgenteDeObjetivos):

    def __init__(self, simbolo, pos, bdi):
        super().__init__(simbolo, pos, bdi)
        bdi.agentesCooperativos.append(self)
        self.recursosConhecidos = bdi.recursosConhecidos

    def definirObjetivoMaisValioso(self) -> tuple[int, int]:
        objetivo = None
        maior_razao = float('inf')
    
        for recurso in self.recursosConhecidos:
            distance = abs(self.x - recurso[0]) + abs(self.y - recurso[1])
            valor = self.carga.valor # valor do recurso
            razao = valor/(2*distance)

            if razao > maior_razao:
                maior_razao = razao
                objetivo = recurso
        print("indo para objetivo escolhido", objetivo)
        return objetivo
    
    def entrouNaBase(self, carga):
        super().entrouNaBase(carga)
        self.objetivo = self.definirObjetivoMaisValioso()

        

    # def receberMensagemCoop(self, recursosConhecidos):
    #     print(" agente cooperativo recebendo a mensagem do bdi")
    #     # Receber uma lista 
    #     # Fazer um calculo para saber qual dos recursos da lista valem mais a pena tornar como objetivo (x = valor do recurso/2* distancia)

    #     # print("lista de recursos:", recursosConhecidos)
    #     melhor_valor = -1
    #     melhor_recurso = None
    #     for recurso in recursosConhecidos:
    #         xA,yA = self.posBase #  pos é posBase??
    #         xB,yB = recurso
    #         distancia =  math.sqrt((xB - xA)**2 + (yB - yA)**2)
    #         valor = self.terreno.value.valor/(2*distancia)
            
    #         if valor > melhor_valor:
    #             melhor_valor = valor
    #             melhor_recurso = recurso
            
    #         if melhor_recurso:
    #             print("Novo objetivo a partir de melhor recurso: ", melhor_recurso)
    #             self.objetivo = melhor_recurso
    #             # acho que nao preciso retornar nada
    #         else: 
    #             print("Nenhum recurso válido")
        

        

        # self.objetivo = local_estrutura
        # return local_estrutura

    # def coletar(self, ambiente):
    #     super().coletar(ambiente)

    #     coordenada = self.objetivo
    #     if coordenada in self.BDI.estruturasConhecidas:
    #         self.BDI.estruturasConhecidas.remove(coordenada)

        # Remover local_estrutura da lista do bdi 
    
    
        
