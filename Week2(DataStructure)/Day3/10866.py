import sys
from collections import deque

N = int(sys.stdin.readline().strip())
commands = list()
q = deque()

for i in range(N):
    commands.append(list(sys.stdin.readline().strip().split()))

for i in commands:
    if i[0] == 'push_front':
        q.appendleft(int(i[1]))
    elif i[0] == 'push_back':
        q.append(int(i[1]))
    elif i[0] == 'pop_front':
        try:
            print(q.popleft())
        except:
            print('-1')
    elif i[0] == 'pop_back':
        try:
            print(q.pop())
        except:
            print('-1')
    elif i[0] == 'size':
        print(len(q))
    elif i[0] == 'empty':
        if len(q) == 0:
            print('1')
        else:
            print('0')
    elif i[0] == 'front':
        if len(q) == 0:
            print('-1')
        else:
            print(q[0])
    elif i[0] == 'back':
        if len(q) == 0:
            print('-1')
        else:
            print(q[-1])