#faça um programa que leia um número inteiro e mostre na tela sua tabuada
i = 1
n = int(input('Digite um número inteiro: '))
print(f'A tabuada de {n} é:')

while i <= 10:
    calc = n * i
    print(f'{n} x {i} = {calc}')
    i+=1