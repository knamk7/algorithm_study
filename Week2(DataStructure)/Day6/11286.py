import sys
import heapq

N = int(input())
pri_que = []

for i in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if len(pri_que):
            print(heapq.heappop(pri_que)[1])
        else:
            print('0')
    elif temp < 0:
        heapq.heappush(pri_que, (-temp, temp))
    else:
        heapq.heappush(pri_que, (temp, temp))