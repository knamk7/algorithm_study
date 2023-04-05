N = int(input())
result = 0

for i in range(1, N+1):
    temp = str(i)
    sum = i
    for j in temp:
        sum += int(j)
    if sum == N: # As result was initialized as 0, only one if is OK.
        result = i
        break

print(result)