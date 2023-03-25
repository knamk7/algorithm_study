N = int(input())
dots = list()

for i in range(N):
    dots.append(list(map(int,input().split())))

dots.sort()
for i in dots:
    print(i[0],i[1])