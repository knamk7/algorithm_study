from collections import deque

N = int(input())
deck = deque()

for i in range(N,0,-1):
    deck.appendleft(i)
    for j in range(i):
        deck.appendleft(deck.pop())

for i in deck:
    print(i, end=' ')