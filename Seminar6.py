a = []
n = int(input('Enter range A: '))
for i in range(n):
    a.append(input('Enter A: '))
b = []
m = int(input('Enter range B: '))
for i in range(m):
    b.append(input('Enter B: '))
print(a, b)
for i in range(len(a)):
    for ii in range(len(b)):
        if a[i] == b[ii]:
            print(a[i])
            break

