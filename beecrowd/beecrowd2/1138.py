def idade_em_dias(anos, meses, dias):
    total = (anos * 365) + (meses * 30) + dias
    return total


ano = int(input())
mes = int(input())
dia = int(input())

print(idade_em_dias(ano,mes,dia))