# Solução Encontro Marcado

## Resolução

O problema foi desenvolvido utilizando a programação dinâmica, que consiste numa estrutura recursiva, resolvendo os subproblemas e fazendo uso de uma variavel auxiliar que armazena os dados.


```python
def encontra_rota(M: int, N: int, L: int, C: int, B: List[Tuple[int, int, int, int]]) -> str:
    ...
return recursive(pos_inicial, M, N, pos_ana, pos_percorridas, B)
```

Essa primeira chamada é o pontapé inicial para que o algoritmo entre em recursividade:

```python
def recursive(pos_atual, M, N, pos_ana, pos_percorridas: Tuple[int,int], rotas_bloqueadas):
    ...
    if pos_atual != pos_ana:
        return recursive(pos_atual, M, N, pos_ana, pos_percorridas, rotas_bloqueadas)
```

Após resolver os problemas, como encontrar as rotas disponíveis, o algoritmo faz a posicao atual percorrer tais rotas até que tenha encontrado a solução
> pos_atual == pos_ana


E retorna os resultados em cascata

##### Algoritmo de rotas
O algoritmo de rotas verifica as rotas possíveis (Norte, Sul, Leste, Oeste) de acordo com a posição atual. Se não houver barreira e tal caminho ainda não foi percorrido, é uma rota disponível
```python
...
if rota not in rotas_bloqueadas and prox_pos not in pos_percorridas:
    rotas_disponiveis.append(rota)
...
```

#### Restrições
Caso o algoritmo de encontrar rotas disponíveis retorne vazio, o caso é impossível:
```python
...
if len(rotas_disponiveis) == 0:
    return 'IMPOSSIVEL'
...
```