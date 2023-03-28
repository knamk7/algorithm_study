import sys

N = int(input()) # the number of inputs
li = list() # a list for saving inputs

for i in range(N): # saving inputs in the list
    li.append(int(sys.stdin.readline()))
    
li.sort()

for i in li:
    print(i)