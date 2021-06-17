# Solução Moedas

## Resolução

O problema foi desenvolvido utilizando algoritmo guloso, ou seja, buscou virar a maior quantidade de moedas possíveis a fim de dexá-las com valor virado para cima. Isso sem se preoucupar tanto com outros possíveis "subproblemas"

É necessário encontrar a primeira moeda com valor virado para baixo
```python
index = len(moedas) - K if moedas.index('C') + K > len(moedas) else moedas.index('C')
```

E então virar as __K__ moedas em sua volta
```python
y = 0
while y < K and (index + y) < len(moedas):
    moedas[index + y] = 'V' if moedas[index + y] == 'C' else 'C'
    y = y + 1
```

#### Restrições
Devido o algoritmo se repetir até que não existam moedas com valor virado para baixo, é necessário algum critério de parada quando o caso for impossível:
```python
if moedas.count('C') == 1 or (len(moedas) == K and moedas.count('C') < len(moedas)):
    return -1
```

Se houver apenas 1 moeda, então é impossível, pois __K__ >= 2
Exemplo:
VVVC
VVCV
VVVC