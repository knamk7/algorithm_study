N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_price = 1000000000
result = 0

for i in range(N-1):
    min_price = min(min_price, prices[i])
    result += min_price * distances[i]

print(result)