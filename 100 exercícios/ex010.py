# Crie um programa que leia quanto dinheiro em reais uma pessoa tem na carteira, e mostre quantos Dólares ela pode comprar

escolha = input('Digite (1) se deseja converter Real em dólar ou (2) se deseja converter dólar em real: ')

if escolha == '1' or escolha == '2':
    if escolha == '1':
        valor = float(input('Digite seu valor em Real: '))
        calcd = valor * 0.18
        print(f'Com {valor} R$ reais você terá {calcd} $ dólares')

    else:
        valor = float(input('Digite seu valor em Dólar: '))
        calcr = valor * 5.5556
        print(f'Com {valor} $ dólares você terá {calcr} R$ reais')
else:
    print('\nReinicie o programa e digite um valor válido: 1 OU 2')


