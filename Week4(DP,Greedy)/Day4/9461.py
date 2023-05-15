def pad(n):
    p = [0,1,1,1,2,2]
    for i in range(6, n+1):
        p.append(p[i-1] + p[i-5])
    return p[n]

N = int(input())

for i in range(N):
    print(pad(int(input())))