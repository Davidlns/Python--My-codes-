def gastos_fixos():

    aluguel = float(400)
    internet = float(100)
    energia = float(200)
    agua = float(40)
    mercado = float(600)
    produtos_limpeza = float(100)
    diversos = float(100)
    parcela_placa_joao = float(250)

    fixos = float(aluguel + internet + energia + agua + mercado + produtos_limpeza + diversos + parcela_placa_joao)

    return fixos

def gastos_cartoes_outros(nu,bb,og):

    calcvariados = float(nu + bb + og)

    return calcvariados


def calc_renda(renda_extra):
    salario_david = 1412
    salario_nay = 650
    bolsa_familia = 600

    renda_mensal = float(salario_nay + salario_david + bolsa_familia + renda_extra)
    return renda_mensal

banco1 = float(input('Informe o valor da sua fatura do banco 1: '))
banco2 = float(input('Informe o valor da sua fatura do banco 2: '))
outros = float(input('Se houverem outros gastos, informe aqui: '))

extra = float(input('Se você obteve alguma renda extra fora da sua renda fixa mensal, informe aqui o valor ganho: '))

gasto_total = float(gastos_fixos() + gastos_cartoes_outros(banco1, banco2, outros))
sobra_mes = float( calc_renda(extra) - gasto_total )

print(f'Seu gasto com despesas fixas mensais é de: {gastos_fixos()}\n Seus gastos variados, com Cartões e outros é de: {gastos_cartoes_outros(banco1,banco2,outros)} \n Sua renda total do é de: {calc_renda(extra)} ')
print(f'A Sua sobra do mês é de {sobra_mes:.2f} ')

