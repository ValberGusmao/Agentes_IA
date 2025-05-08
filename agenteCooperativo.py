from agenteDeObjetivos import AgenteDeObjetivos


class AgenteCooperativo(AgenteDeObjetivos):
    def receberMensagem(self):
        print(" agente cooperativo recebendo a mensagem do bdi")
        local_estrutura = self.BDI.enviarMensagemBDI
        
        print("coordenada:", local_estrutura)
        self.objetivo = local_estrutura
        return local_estrutura

    
    
        
