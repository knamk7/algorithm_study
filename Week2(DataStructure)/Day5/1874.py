# 못 푼 문제
# stack 마지막 값이 target에 있으면 pop
# 없으면 stack에 자연수를 오름차순으로 push
# target이 안만들어지면 print('NO')

import sys

N = int(input())
target = list()
stack = []
result = list()

for i in range(N):
    target.append(int(sys.stdin.readline().strip()))

temp = 1
for i in target:
    stack.append(temp)
    while i > stack[-1]:
        temp += 1
        stack.append(temp)
        result.append('+')

for i in result:
    print(i)