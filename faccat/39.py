inventario = ['Laptop', 'Mouse', 'Monitor', 'Keyboard']

for i in inventario:
    if i == 'Tablet':
        value = True
    else:
        value = False
    
if value:
    print(f'Is Tablet in inventory? True')
else:
    print(f'Is Tablet in inventory? False')