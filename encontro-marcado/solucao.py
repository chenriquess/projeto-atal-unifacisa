from typing import List, Tuple


def encontra_rota(M: int, N: int, L: int, C: int, B: List[Tuple[int, int, int, int]]) -> str:
    pos_inicial = (0,0)
    pos_percorridas = [(0,0)]
    pos_ana = (L, C)

    return recursive(pos_inicial, M, N, pos_ana, pos_percorridas, B)

    pass
    
def recursive(pos_atual, M, N, pos_ana, pos_percorridas: Tuple[int,int], rotas_bloqueadas):
    rotas_disponiveis = get_prox_rotas(pos_atual, M, N, pos_percorridas, rotas_bloqueadas)
    
    if len(rotas_disponiveis) == 0:
        return 'IMPOSSIVEL'
    
    pos_atual = (rotas_disponiveis[0][2], rotas_disponiveis[0][3])
    pos_percorridas.append(pos_atual)

    if pos_atual != pos_ana:
        return recursive(pos_atual, M, N, pos_ana, pos_percorridas, rotas_bloqueadas)
    
    return rota_tradutor(pos_percorridas)

def get_prox_rotas(pos_atual, M, N, pos_percorridas, rotas_bloqueadas):
    rotas_disponiveis = []

    def prox_rota_pos(x,y):
        dif_x = (M - 1) - pos_atual[0] + x
        dif_y = (N - 1) - pos_atual[1] + y
        new_pos_x = pos_atual[0] + x if pos_atual[0] + x < M else (pos_atual[0] + x) - dif_x
        new_pos_y = pos_atual[1] + y if pos_atual[1] + y < N else (pos_atual[1] + y) - dif_y
        
        return (max(0, new_pos_x), max(0, new_pos_y))

    proximas_rotas = [
        pos_atual + prox_rota_pos(1, 0), # Sul
        pos_atual + prox_rota_pos(-1, 0), # Norte
        pos_atual + prox_rota_pos(0,1), # Leste
        pos_atual + prox_rota_pos(0,-1) # Oeste
    ]
    
    for rota in proximas_rotas:
        prox_pos = (rota[2], rota[3])

        if rota not in rotas_bloqueadas and prox_pos not in pos_percorridas:
            rotas_disponiveis.append(rota)

    return rotas_disponiveis

def rota_tradutor(pos_percorridas) -> str:
    coord = ''
    
    def coord_char(pos1, pos2) -> str:        
        if pos1[1] == pos2[1]:
            return 'N' if pos2[0] - pos1[0] == -1 else 'S'
        elif pos1[0] == pos2[0]:
            return 'O' if pos2[1] - pos1[1] == -1 else 'L'
        else:
            return 'ERRO'
    
    x = 0
    while x < len(pos_percorridas) - 1:
        x = x + 1
        coord = coord + coord_char(pos_percorridas[x-1],pos_percorridas[x])

    return coord

if __name__ == "__main__":
    help(encontra_rota)