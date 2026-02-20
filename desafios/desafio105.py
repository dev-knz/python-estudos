# Faça um programa que tenha um função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notas(*num, sit=False):
    boletim = dict()
    media = 0
    boletim['qntd'] = len(num)

    for i in range(0, len(num)):
        if i == 0:
            maior = menor = num[i]
            media += num[i]
        
        if num[i] > maior:
            maior = num[i]
            media += num[i]
        
        if num[i] < menor:
            menor = num[i]
            media += num[i]
    
    media = media / len(num)
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['media'] = media

    if (sit==True):
        if media > 6.9:
            boletim['situacao'] = 'Boa'
        else:
            boletim['situacao'] = 'Ruim'
    
    print(boletim)


notas(7,5,9,sit=True)



