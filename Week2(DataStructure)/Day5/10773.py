import sys

K = int(sys.stdin.readline().strip())
stack = list()
sum = 0

for i in range(K):
    temp = int(sys.stdin.readline().strip())
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)

for i in stack:
    sum += i

print(sum)