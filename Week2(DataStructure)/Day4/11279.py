import sys
import heapq # default is minheap

N = int(sys.stdin.readline().strip())
heap = []

for i in range(N):
    temp = int(sys.stdin.readline().strip())
    if temp == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print('0')
    else:
        heapq.heappush(heap, [-temp, temp])