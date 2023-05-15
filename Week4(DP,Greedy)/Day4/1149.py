# greedy, incorrect approach

N = int(input())
cost = [0]
result = 0
last = -1

for i in range(N):
    cost.append(list(map(int, input().split())))

for i in range(1,N+1):
    if last != i.index(min(i)):
        result += min(i)
        last = i.index(min(i))
    else:
        result += sorted(i)[1]
        last = i.index(sorted(i)[1])

print(result)