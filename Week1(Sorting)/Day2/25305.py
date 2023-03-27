N, k = map(int, input().split())
li = list(map(int,input().split()))

li.sort()
print(int(li[N-k]))