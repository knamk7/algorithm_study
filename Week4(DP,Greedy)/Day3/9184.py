# Not working properly

def w(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        return 1
    elif (a > 20) or (b > 20) or (c > 20):
        return w(20, 20, 20)
    data = [[[0]*(c+1)]*(b+1)]*(a+1)
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if (i == 0) or (j == 0) or (k == 0):
                    data[i][j][k] = 1
                elif (i < j) and (j < k):
                    data[i][j][k] = data[i][j][k-1] + data[i][j-1][k-1] - data[i][j-1][k]
                else:
                    data[i][j][k] = data[i-1][j][k] + data[i-1][j-1][k] + data[i-1][j][k-1] - data[i-1][j-1][k-1]
    return data[a][b][c]

while 1:
    a, b, c = map(int, input().split())
    if (a == -1) and (b == -1) and (c == -1):
        break
    else:
        print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))