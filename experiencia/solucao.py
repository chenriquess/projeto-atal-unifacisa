from typing import List, Tuple
from queue import PriorityQueue

class Prato:
    def __init__(self, nome, prato_valor, experiencia):
        self.nome = nome
        self.prato_valor = prato_valor
        self.experiencia = experiencia

    def __str__(self):
        return f"{self.nome}"


class Experiencia:
    def __init__(self, valor_limite, pratos, pratos_disponiveis):
        self.pratos = pratos
        self.pratos_disponiveis = pratos_disponiveis
        self.prato_valor = sum([objeto.prato_valor for objeto in pratos])
        self.experiencia = sum([objeto.experiencia for objeto in pratos])
        proporcoes = [objeto.prato_valor/objeto.experiencia for objeto in pratos_disponiveis] + [0]
        melhor_proporcao = max(proporcoes)
        self.melhor_possivel = self.experiencia + (valor_limite - self.prato_valor) * melhor_proporcao

    # Métodos de comparação de objetos
    def __ge__(self, other):
        return self.melhor_possivel <= other.melhor_possivel

    def __gt__(self, other):
        return self.melhor_possivel < other.melhor_possivel

    def __repr__(self):
        itens = ([str(objeto.nome) for objeto in self.pratos])
        return itens


class PratoBnB:
    def __init__(self, valor_limite, pratos_disponiveis):
        self.valor_limite = valor_limite
        self.pratos_disponiveis = pratos_disponiveis
        

    def resolver(self, verbose=False):
        raiz = Experiencia(self.valor_limite, [], self.pratos_disponiveis)
        melhor_solucao = raiz
        fila = PriorityQueue()
        fila.put(raiz)

        while not fila.empty():
            proximo = fila.get()
            if proximo.melhor_possivel <= melhor_solucao.experiencia or proximo.prato_valor > self.valor_limite:
                continue
            if proximo.prato_valor > melhor_solucao.prato_valor:
                melhor_solucao = proximo
            n_opcoes = len(proximo.pratos_disponiveis)
            for i in range(n_opcoes):
                objeto_escolhido = proximo.pratos_disponiveis.pop(i)
                fila.put(Experiencia(self.valor_limite, proximo.pratos + [objeto_escolhido], list(proximo.pratos_disponiveis)))
                proximo.pratos_disponiveis.insert(i, objeto_escolhido)

        return melhor_solucao


def melhor_experiencia(L: int, C: List[Tuple[str, int, int]]) -> List[str]:
    mb = PratoBnB(L, [Prato(item[0], item[1], item[2]) for item in C])
    pratos_escolhidos = [prato.nome for prato in mb.resolver().pratos]

    return pratos_escolhidos
    

if __name__ == "__main__":
    help(melhor_experiencia)