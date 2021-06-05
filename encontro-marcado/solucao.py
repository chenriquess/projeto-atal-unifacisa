from typing import List, Tuple


def encontra_rota(M: int, N: int, L: int, C: int, B: List[Tuple[int, int, int, int]]) -> str:
    """Função que calcula uma rota entre as coordenadas (0, 0) e as coordenadas
    (L, C), em um grid de tamanho MxN, levando em consideração trechos que estão
    em obras, indicados na variável B.

    Parâmetros
    ----------
    M, N : int
        Dimensões do mapa da cidade.

    L, C : int
        Coordenadas do destino (L, C).

    B: List[Tuple[int, int, int, int]]
        Array com localização dos trechos em obras na cidade.

    Retorna
    -------
    Uma string indicando a direção de cada movimento feito no trajeto, ou
    "IMPOSSIVEL", caso não seja possível traçar uma rota.
    """
    pass


if __name__ == "__main__":
    help(encontra_rota)
