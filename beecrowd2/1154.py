def cel2far(celsius):
    f = (9.0/5.0) * celsius + 32
    return f

n = int(input())

f = cel2far(n)
print(f'{n:.2f} {f:.2f}')