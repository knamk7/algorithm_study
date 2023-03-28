N = int(input())
li1 = list(map(int, input().split()))
li2 = sorted((set(li1)))
li3 = [0] * N
k = 0

for i in li2:
    while i in li1:
        temp = li1.index(i)
        li3[temp] = k
        li1[temp] = 10000000000
    k += 1

for i in li3:
    print(i, end=' ')