N = int(input())
datalist = set(map(int, input().split()))
M = int(input())
testlist = list(map(int, input().split()))

for i in testlist:
    if i in datalist:
        print('1', end=' ')
    else:
        print('0', end=' ')