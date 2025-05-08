from agenteDeObjetivos import AgenteDeObjetivos


class AgenteCooperativo(AgenteDeObjetivos):
    def receberMensagemCoop(self):
        print(" agente cooperativo recebendo a mensagem do bdi")
        local_estrutura = self.BDI.enviarMensagemBDI
        
        print("coordenada:", local_estrutura)
        self.objetivo = local_estrutura
        return local_estrutura

    def coletar(self, ambiente):
        super().coletar(ambiente)

        coordenada = self.receberMensagemCoop()
        if coordenada in self.BDI.estruturasConhecidas:
            self.BDI.estruturasConhecidas.remove(coordenada)

        # Remover local_estrutura da lista do bdi 
    
    
        
