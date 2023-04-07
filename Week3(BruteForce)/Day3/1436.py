N = int(input())
title = [0]
i = 666
while len(title) < N+1:
    temp = str(i)
    for j in range(2, len(temp)):
        if temp[j-2] == '6' and temp[j-1] == '6' and temp[j] == '6':
            title.append(i)
            break
    i += 1

print(title[N])