from tipoTerreno import *
    
class ElementoMapa():
    def __init__(self, terreno:Tipo = Tipo.LIVRE):
        self.terreno = terreno
        self.agentes = []
    
    def adicionarAgente(self, entidade):
        if entidade not in self.agentes:
            self.agentes.append(entidade)

    def posicionarElemento(self, elemento: Tipo):
        self.terreno = elemento

    def moverAgente(self, ent, proximaPosicao: 'ElementoMapa'):
        proximaPosicao.agentes.append(ent)
        # if ent in self.entidades: Ajuda a identificar erros isso não esta sendo verificado
        self.agentes.remove(ent)

    #Retornar maior que 0 se o recurso ali foi coletado
    #Retorna tbm qual o novo tipo de terreno que deve ser substituido
    def removerRecurso(self) -> tuple[int, Tipo]:
        valor = self.terreno.value.valor
        tipo:Tipo = self.terreno

        if self.terreno == Tipo.ESTRUTURA:
            #Se não tiver agentes suficientes no lugar nada acontecerá
            if len(self.agentes) < 2:
                valor = 0
            #Porém se houver agentes, ambos devem ganhar os pontos
            else:
                tipo = Tipo.ESTRUTURA_PRE_COLETADA
        #Só é recurso se o valor for maior que 0
        elif valor > 0:
            tipo = Tipo.LIVRE
        return (valor, tipo)

    #Usado pelo view. Mudado pela separação na hora de desenhar recursos e agentes
    def getElemento(self) -> "ElementoMapa":
        # if self.agentes:
            # return self.agentes[0]
        return self.terreno

    def __str__(self):
        if self.agentes:
            return str(self.agentes[0])
        return str(self.terreno.value)