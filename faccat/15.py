hora_ini = int(input())

hora_fin = int(input())

if hora_fin < hora_ini:
    hora = 24 + (hora_fin - hora_ini)
    print(hora)
else:
    hora = (hora_ini - hora_fin)
    print(hora)