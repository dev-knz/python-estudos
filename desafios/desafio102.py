# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico opcional indicando se será mostrado ou não na telao processo de cálculo do fatorial

def fatorial(num, show = False):
    c = 1
    for i in range(num, 0, -1):
        c *= i
    if show == False:
        print(c)
        print(f'O número fatorial é de: {c}')
    else:
        for i in range(num, 0, -1):
            if i == num:
                print(num, end=' x ')
            elif i > 0 and i != 1:
                num -= 1
                print(num, end=' x ')
            elif i == 1:
                num -= 1
                print(f'{num} = {c}')
                break

fatorial(7, True)