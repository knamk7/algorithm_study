from collections import deque

[N, M] = list(map(int, input().split()))
locations = list(map(int, input().split()))

a = deque(range(1, N + 1))
counts = 0

for i in locations:
    if a.index(i) > N/2:
        while a[0] != i:
            a.appendleft(a.pop())
            counts += 1
        a.popleft()
        N -= 1
    else:
        while a[0] != i:
            a.append(a.popleft())
            counts += 1
        a.popleft()
        N -= 1

print(counts)