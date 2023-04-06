N = int(input())
data = []
ranks = []
for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(N):
    temp = 1
    for j in range(N):
        if i == j:
            continue
        elif data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            temp += 1
    ranks.append(temp)

for i in ranks:
    print(i, end=' ')