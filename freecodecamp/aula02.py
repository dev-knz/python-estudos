name = "Beau"
print(type(name))
print(isinstance(name, int))  


t1 = True
t2 = False

read = any([t1, t2]) # Verify the sentences, one True return True
print(read)

read2 = all([t1, t2]) # Verify all paramers.
print(read2)

num1 = 2 + 3j
num2 = complex(2, 3)

print(num1.real, num1.imag)
print(num2.real, num2.imag)