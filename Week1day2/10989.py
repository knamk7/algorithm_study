N = int(input())
li = [0]*10001
element = 1

for i in range(N):
    li[int(input())] += 1

for i in li:
    for j in range(i):
        print(element)
    element += 1