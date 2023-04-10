N = int(input())
final = [N]

for i in range(1, N+1):
    temp = [N, i]
    k = temp[0] - temp[1]
    while(k >= 0):
        if k < 0:
            break
        else:
            temp.append(k)
            k = temp[-2] - temp[-1]
    if len(temp) > len(final):
        final = temp

print(len(final))
for i in final:
    print(i, end=' ')