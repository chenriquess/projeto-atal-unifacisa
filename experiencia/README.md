# Experiência Gastronômica

Após um grande esforço, Joãozinho conseguiu encontrar-se com sua amiga, Aninha,
e ambos decidiram sair para jantar em um excelente restaurante -- no mesmo
quarteirão onde estavam, para evitar possíveis bloqueios no trânsito -- chamado
de **The U**.

Os pratos do **The U**, estão entre os melhores do mundo. Cada um deles
proporciona uma experiência única para os seus clientes o que os deixa sempre
com dúvidas sobre qual escolher. Para ajudar os seus clientes, o restaurante
preparou um cardápio que traz, junto ao nome dos pratos, o valor **V** cobrado
pelo mesmo, e a experiência gastronômica **E** proporcionada pelo seu consumo.

Joãozinho quer ter a melhor (maior) experiência gastronômica possível, sem
repetir nenhum prato. Além disso, como você sabe, Joãozinho tem uma quantidade
**L** limitada de dinheiro, que ele juntou durante os últimos anos, então deve
escolher sabiamente quais pratos pedir.

Implemente a função _melhor_experiencia_ que recebe as variáveis:

- **L** - o valor que Joãozinho tem disponível para gastar no restaurante;
- **C** - o cardápio descrito como uma lista de tuplas (n<sub>i</sub>,
  v<sub>i</sub>, e<sub>i</sub>), onde:
  - n<sub>i</sub> é o nome do i-ésimo prato no cardápio;
  - v<sub>i</sub> é o valor do i-ésimo prato no cardápio;
  - e<sub>i</sub> é a experiência gastronômica do i-ésimo prato no cardápio;

A função deve retornar uma lista contendo o nome dos pratos escolhidos, de forma
a obter a melhor experiência gastronômica possível. Os nomes presentes na
lista retornada não precisam obedecer nenhuma ordem específica.

## Entrada

A entrada consiste das variáveis **L** e **C**, conforme descritas
anteriormente.****

## Saída

A função deve retornar uma lista com os nomes de todos os pratos escolhidos por
Joãozinho, de modo a ter a melhor experiência gastronômica possível. A ordem dos
alimentos na lista não importa.

## Exemplos

| **L** | **C** | **Saída** |
| --- | --- | --- |
| 100 | \[("Caviar", 100, 20), ("Pizza", 20, 5), ("Bode", 11, 10), ("Lagosta", 90, 15)\] | \["Caviar"\] |
| 110 | \[("Caviar", 100, 20), ("Pizza", 20, 5), ("Bode", 11, 10), ("Lagosta", 90, 15)\] | \["Bode", "Lagosta"\] |
| 120 | \[("Caviar", 100, 20), ("Pizza", 20, 5), ("Bode", 11, 10), ("Lagosta", 90, 15)\] | \["Caviar", "Bode"\] |


### Explicação

Em todos os três casos, nós temos os seguintes pratos

| Nome | Valor | Experiência Gastronômica |
| --- | --- | --- |
| Caviar | 100 | 20 |
| Pizza | 20 | 5 |
| Bode | 11 | 10 |
| Lagosta | 90 | 15 |

No primeiro caso, a melhor experiência gastronômica que Joãzinho poderia ter é
igual a 20, escolhendo apenas o primeiro prato, que é de Caviar, e tendo um
custo total de 100.

No segundo caso, a melhor experiência é igual a 25, escolhendo Bode e Lagosta, e
tendo um custo total igual a 101.

No terceiro caso, a melhor experiência é igual a 30, escolhendo Caviar e Bode, e
tendo um custo total de 111. 

## Dica

Para este problema, a técnica a ser utilizada é de *branch and bound*.
