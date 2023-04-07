l = list()
for i in range(9):
    l.append(int(input()))
heights_sum = sum(l)
state = 0
goal = heights_sum - 100
for i in range(8):
    for j in range(i+1,9):
        if (l[i] + l[j]) == goal:
            l.pop(j)
            l.pop(i)
            state = 1
            break
    if state == 1:
           break

l.sort()
for i in l:
    print(i)