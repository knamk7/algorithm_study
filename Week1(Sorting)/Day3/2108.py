import sys
from collections import Counter

N = int(input())
li = list()

for i in range(N):
    li.append(int(sys.stdin.readline()))

li.sort()
count = Counter(li).most_common(2)

print(round(sum(li)/N))
print(li[N//2])
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])
print(li[N-1]-li[0])