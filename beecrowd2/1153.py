n1, n2 = map(int, input().split())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l3 = []
for i in range(n2):
    for j in range(n1):
        if l2[i] == l1[j]:
            l3.append(l2[i])
if l3 == l2:
    print('S')
else:
    print('N')
        
    
              

