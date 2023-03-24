index = 0
a = input()
b = list()
c = [0] * 10

for i in a:
    b.append(int(i))
for i in range(10):
    for j in b:
        if i == j:
            c[i] += 1
c.reverse()
nine = 9
for i in c:
    print(str(nine) * i, end='')
    nine -= 1