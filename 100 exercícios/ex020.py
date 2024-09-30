# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro e mostre a ordem sorteada

from random import sample

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

random = [aluno1,aluno2,aluno3,aluno4]

print(f'Ordem aleatória de apresentação: {sample(random, k=4)}') #Realiza ordem aleatória dos itens da lista sem repetir nenhum item, e apresentando 4 itens (k=4)