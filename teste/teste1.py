# Fazer uma calculadora

i = 0
for i in range(0, 999):

    print('1) Somar')
    print('2) Subtrair')
    print('3) Multiplicar')
    print('4) Dividir')      
    esc = int(input('Escolha qual opção você quer realizar '))

    n1 = int(input('Insira o primeiro valor '))
    n2 = int(input('Insira o segundo valor '))

    if esc == 1:
        print(f'A soma desses valores é {n1+n2}')
    if esc == 2:
        print(f'A subtração desses valores é {n1-n2}')
    if esc == 3:
        print(f'A multiplicação desses valores é {n1*n2}')
    if esc == 4:
        print(f'A divisão desses valores é {n1/n2}')
    if esc > 4 or esc < 1:
        print(f'Insira um valor que exista. ')

    con = input('Deseja continuar com as operações?\nSim\nNao ')
    con = con.upper()

    if con == 'NAO':
        break
        







