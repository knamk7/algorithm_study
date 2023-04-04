N, K = map(int, input().split())
cointypes = []
nums_of_coins = 0

for i in range(N):
    cointypes.append(int(input()))

for i in range(N):
    temp = cointypes.pop()
    nums_of_coins += K//temp
    K = K % temp

print(nums_of_coins)