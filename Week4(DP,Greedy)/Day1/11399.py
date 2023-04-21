N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
result = 0
for i in range(N):
    result += time_list[i]*(N-i)
print(result)