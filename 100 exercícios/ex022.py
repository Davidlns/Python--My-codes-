#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todos minúsculos
# Quantas letras tem ao todo sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ') #recepção do nome completo do usuário

nome = nome.upper()
print(f'\n\n Nome maiúsculo: {nome}')

nome = nome.lower()
print(f'\n\n Nome minúsculo: {nome}')

nome2 = nome.replace(" ","")
print(f"\n\n O nome tem {len(nome)} letras sem contar os espaços")

lista = nome.split()
print(f'\n\nO primeiro nome tem {len(lista[0])} letras')
