import sys

N = int(input())
target = []
stack = [0]
result = []

for i in range(N):
    target.append(int(sys.stdin.readline().strip()))

temp = 0
for i in target:
    while i > stack[-1]:
        temp += 1
        stack.append(temp)
        result.append('+')
    if stack.pop() == i:
        result.append('-')
    else:
        result = ['NO']
        break

for i in result:
    print(i)