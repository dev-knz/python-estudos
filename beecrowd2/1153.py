def mediaAR(media, notaAP):
    if notaAP >= media:
        return True
    return False

media, nota = input().split()

media = float(media)
nota = float(nota)

if mediaAR(media, nota):
    print('Aprovado')
else:
    print('Reprovado')