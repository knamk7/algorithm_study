from collections import deque

N = int(input())
numbers_of_slices = list(map(int, input().split()))
data = deque()
results = [0]* N

for i in range(N):
    data.append([i, numbers_of_slices[i]])

t = 0

while len(data) > 0:
    temp = data.popleft()
    t += 1
    if temp[1] > 1:
        temp[1] -= 1
        data.append(temp)
    else:
        results[temp[0]] = t

for i in results:
    print(i, end=' ')