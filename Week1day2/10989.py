N = int(input())
li = [0]*10000
index = 1

for i in range(N):
    li[int(input())-1] += 1

for i in li:
    for j in range(i):
        print(index)
    index += 1