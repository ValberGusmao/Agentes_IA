from agenteDeObjetivos import AgenteDeObjetivos


class AgenteCooperativo(AgenteDeObjetivos):

    def __init__(self, simbolo, pos, bdi):
        super().__init__(simbolo, pos, bdi)
        bdi.agentesCooperativos.append(self)

    def receberMensagemCoop(self, local_estrutura):
        print(" agente cooperativo recebendo a mensagem do bdi")
        
        print("coordenada:", local_estrutura)
        self.objetivo = local_estrutura
        return local_estrutura

    def coletar(self, ambiente):
        super().coletar(ambiente)

        coordenada = self.objetivo
        if coordenada in self.BDI.estruturasConhecidas:
            self.BDI.estruturasConhecidas.remove(coordenada)

        # Remover local_estrutura da lista do bdi 
    
    
        
