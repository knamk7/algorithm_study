N = int(input())
sum = 0
temp = 0
count = 0
input_list = list()
saving_list = [0] * 8001

for i in range(N):
    temp = int(input())
    sum += temp
    input_list.append(temp)
    saving_list[temp+4000] += 1

input_list.sort()
print(round(sum/N))
print(input_list[N//2])

m = max(saving_list)
sum = -4001
temp = 0
for i in saving_list:
    sum += 1
    if i == m:
        count += 1
        if count == 2:
            temp = sum
            break
        else:
            temp = sum

print(temp)
print(input_list[N-1]-input_list[0])