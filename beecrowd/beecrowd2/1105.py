n = int(input())

t = list()
entrada = input().split()

for i in range(len(entrada)):
    t.append(int(entrada[i]))
    
p = int(input())
m = int(input())

m_aux, p_aux = 0, 0

for i in range(n):
    if t[i] == 1:
        p_aux += 1
    else:
        m_aux += 1

if p_aux <= p and m_aux <= m:
    print('S')
else:
    print('N')