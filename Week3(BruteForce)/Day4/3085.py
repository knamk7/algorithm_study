# 미완성, 나중에할거
N = int(input())
candies_original = list[]

for i in range(N):
    candies_original.append(input())

max = 1
for i in range(N):
    for j in range(N):
        candies = candies_original
        try:
            if candies[i][j] != candies[i][j+1]:
                temp = candies[i][j+1]
                candies[i][j+1] = candies[i][j]
                candies[i][j] = temp