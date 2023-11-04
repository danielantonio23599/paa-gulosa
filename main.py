print(' Problema BeeCrowd Programação Gulosa ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de PAA')
print('Autores: Daniel Antônio de Sá')
while True:
    N, D = map(int, input().split()) # entrada dos numeros e digitos
    if N == 0 and D == 0:
        break
    num = input().strip()
    final = [] # array de numeros final
    removido = 0
    for digito in num: # percorre o vetor
        # se a quantidade de removidos tiver chagado até a D = a necessaria e
        # final for diferente de vazio e a ultima posição do final form menor digito
        while removido < D and final and final[-1] < digito:
            final.pop()
            removido += 1
        final.append(digito)

    # Se ainda for necessario remover mais dígitos, remova a partir do final do vetor
    while removido < D:
        final.pop()
        removido += 1
    print("".join(final))
