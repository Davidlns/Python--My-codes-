#Receba 4 nomes e realize um sorteio que retorne sempre um resultado aleatório usando os 4

from random import choice

alunoa = input('Digite o nome do primeiro aluno: ')
alunob = input('Digite o nome do segundo aluno: ')
alunoc = input('Digite o nome do terceiro aluno: ')
alunod = input('Digite o nome do quarto aluno: ')

lista = [alunoa, alunob, alunoc, alunod]

print(f'O aluno sorteado é: {choice(lista)}')