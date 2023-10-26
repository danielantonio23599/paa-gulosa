from solver import Solver


print(' Problema BeeCrowd Programação Gulosa ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de PAA')
print('Autores: Daniel Antônio de Sá')
# Entrada
linha2 = input("Digite a quantidade de digitos do (numero) seguido pela quantidadee que serão removidos").strip()
linha = input("Digite o numero").strip()
solver = Solver()
# Saída
print(solver.maior_numero_possivel(linha, linha2[0]))
