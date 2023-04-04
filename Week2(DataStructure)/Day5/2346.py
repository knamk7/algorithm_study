from collections import deque

N = int(input())
commands = list(map(int, input().split()))
balloons = deque()
result = list()

for i in range(N):
    balloons.append((i + 1, commands[i]))

for i in range(N):
    temp = balloons.popleft()
    result.append(temp)
    if len(balloons) > 0:
        if temp[1] > 0:
            for j in range(temp[1]-1):
                balloons.append(balloons.popleft())
        else:
            for j in range(-temp[1]):
                balloons.appendleft(balloons.pop())

for i in result:
    print(i[0], end=' ')