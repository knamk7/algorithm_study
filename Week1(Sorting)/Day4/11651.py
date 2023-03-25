N = int(input())
dots = list()

for i in range(N):
    temp = list(map(int,input().split()))
    temp.reverse()
    dots.append(temp)

dots.sort()
for i in dots:
    print(i[1],i[0])