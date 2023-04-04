from collections import deque

[N, K] = list(map(int, input().split()))
K -= 1

nums = deque()
results = []

for i in range(1, N+1):
    nums.append(i)

while(len(nums) > 0):
    for i in range(K):
        nums.append(nums.popleft())
    results.append(nums.popleft())

print('<',end='')
for i in results[:-1]:
    print(i, end=', ')
print(results[-1], end='>')