import sys
import heapq

N = int(input())
data = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N-1):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in temp:
        heapq.heappushpop(data, j)

print(heapq.heappop(data))