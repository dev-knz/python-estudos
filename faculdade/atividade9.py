
for i in range(1, 6):
    for l in range(1, 6):
        if i == l:
            print('[x]', end=' ')
        else:
            print('[ ]', end=' ')
        
        if l == 5:
            print()