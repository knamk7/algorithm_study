T = int(input())
string = list()
for i in range(T):
    string.append(list(input()))
for i in string:
    a = 0
    for j in range(len(i)):
        temp = i.pop()
        if temp == ')': a += 1
        else: a -= 1
        if a < 0: break
    if a < 0:
        print('NO')
    elif a == 0:
        print('YES')
    elif a != 0:
        print('NO')