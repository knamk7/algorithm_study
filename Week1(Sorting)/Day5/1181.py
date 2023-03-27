N = int(input())
li = list()

for i in range(N):
    li.append(input())

for i in sorted(set(li), key= lambda x: (len(x), x)):
    print(i)