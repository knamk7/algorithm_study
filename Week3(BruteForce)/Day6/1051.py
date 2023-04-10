N, M = map(int, input().split())
numarray = []

for i in range(N):
    numarray.append(input())

side = 0

for n in range(N):
    for m in range(M):
        for k in range(min(N - n, M - m)):
            if numarray[n][m] == numarray[n+k][m] and numarray[n][m] == numarray[n][m+k] and numarray[n][m] == numarray[n+k][m+k]:
                side = max(side, k)

print((side+1)**2)