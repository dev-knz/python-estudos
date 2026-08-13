l1, l2 = list(), list()

entrada = input().split()
for i in range(len(entrada)):
    l1.append(int(entrada[i]))
entrada = input().split()
for i in range(len(entrada)):
    l2.append(int(entrada[i]))

l3 = list()
for i in range(len(l1)):
    l3.append(int(l1[i]))
    l3.append(int(l2[i]))

for i in range(len(l3)):
    print(l3[i], end=' ')
    