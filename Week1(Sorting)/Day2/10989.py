import sys

N = int(input())
li = [0]*10001 # Instead of storing values directly in the list, store the number of each value.
element = 0 # For fewer computation, one more element is declared in the list. Original code had 10000 elements in the list.

for i in range(N):
    li[int(sys.stdin.readline())] += 1 # It is faster than normal input(). Deleted +1 by adding index of 0 into the list.

for i in li:
    for j in range(i):
        print(element)
    element += 1