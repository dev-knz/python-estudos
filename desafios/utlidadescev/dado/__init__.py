def leiaDinheiro(msg):
    validacao = input(msg)

    try:
        validacao = int(validacao)
        return validacao
    except ValueError:
        print('Valor inválido.')