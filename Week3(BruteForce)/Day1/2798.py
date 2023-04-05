N, M = map(int, input().split())
cards = []
sum = 0

for i in list(map(int, input().split())):
    if i < M:
        cards.append(i)

for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            temp = cards[i] + cards[j] + cards[k]
            if (temp <= M) and (M - temp < M - sum):
                sum = temp
            if sum == M:
                break
        if sum == M:
            break
    if sum == M:
        break

print(sum)