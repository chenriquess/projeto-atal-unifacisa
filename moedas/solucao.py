def minimo_operacoes(D: str, K: int) -> int:
    contador = 0
    moedas = list(D) # String eh imutavel, portanto lista

    # Enquanto houver moedas com valor para baixo
    while 'C' in moedas:
    
        # Foram estabelecidas 2 condicoes para casos impossiveis
        # Condicao 1:
        # Caso tenha apenas uma moeda, nao eh possivel, pois no minimo 2 serao viradas simultaneamente
        # Foi possivel notar que em algum momento alterando as moedas, isso ocorre nos casos impossiveis
        # Condicao 2:
        # No caso de virar todas as moedas ao mesmo tempo, mas nem todas sejam C, eh impossivel
        if moedas.count('C') == 1 or (len(moedas) == K and moedas.count('C') < len(moedas)):
            return -1

        # IndiceC = Indice da primeira moeda C encontrada ou o ultimo indice - K
        # Assim, eh possivel alterar K moedas em volta de C
        index = len(moedas) - K if moedas.index('C') + K > len(moedas) else moedas.index('C')

        # A partir do indiceC, vira K moedas
        y = 0
        while y < K and (index + y) < len(moedas):
            moedas[index + y] = 'V' if moedas[index + y] == 'C' else 'C'
            y = y + 1
        
        contador = contador + 1

    return contador
    

    pass

if __name__ == "__main__":
    help(minimo_operacoes)