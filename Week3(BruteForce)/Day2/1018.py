N, M = map(int, input().split())
board = []
chess = ['BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB']

for i in range(N):
    board.append(input())

mincount = 64

for i in range(N-7):
    for j in range(M-7):
        count = 0
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l] != chess[k][l]:
                    count += 1
        mincount = min(mincount, count, 64 - count)

print(mincount)