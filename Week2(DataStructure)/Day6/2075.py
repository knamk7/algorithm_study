# 못 푼 문제

import sys
import heapq as h

N = int(input())
data = []

for i in range(N-5):
    sys.stdin.readline()
for i in range(5): # Only last 5 lines matter
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in temp:
        h.heappush(data, (-j, j))

h.heappop(data)
h.heappop(data)
h.heappop(data)
h.heappop(data)
print(h.heappop(data)[1])