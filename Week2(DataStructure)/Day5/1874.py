# 못 푼 문제
# stack 마지막 값이 target에 있으면 pop
# 없으면 stack에 자연수를 오름차순으로 push
# target이 안만들어지면 print('NO')

import sys

N = int(input())
target = list()
stack = [1]
result = list()

for i in range(N):
    target.append(int(sys.stdin.readline().strip()))

n = 2
i = 0

while(1):
    if stack[-1] == target[i]:
        stack.pop()
        result.append('-')
        i += 1
    elif N >= n and stack[-1] != target[i]:
        stack.append(n)
        result.append('+')
    else:
        print('NO')

for i in result:
    print(i, end=' ')