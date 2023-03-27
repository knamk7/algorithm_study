N = int(input())
li = list()

for i in range(N):
    li.append(input().split())

for i in sorted(li, key= lambda x: int(x[0])):
    print(i[0],i[1])