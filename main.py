"""
Crie um programa para encontrar a sub-sequência contínua dentro do array A que possua maior soma:
• Exemplo 1:
o Input: [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]
o Output: 13
Neste primeiro exemplo, o subarray [5, 2, 1, 4, -7, 8] é a sequência contínua de maior soma contida dentro do array e a soma deste array é 13
• Exemplo 2:
o Input: [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]
o Output: 8
Neste segundo exemplo, o subarray [5, -1, 2, 1, 1] é a sequência contínua de maior soma contida dentro do array e a soma destes número é 8.
Seu programa só precisa exibir o VALOR da maior soma, não é necessário exibir o array em questão.
"""


def kadane(lista, tam):
    max_ate_agora = lista[0]
    max_final = 0

    for i in range(0, tam):
        max_final = max_final + lista[i]
        if max_final < 0:
            max_final = 0
        elif max_ate_agora < max_final:
            max_ate_agora = max_final

    return max_ate_agora


lista = [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]
print("Máximo soma contida é", kadane(lista, len(lista)))
