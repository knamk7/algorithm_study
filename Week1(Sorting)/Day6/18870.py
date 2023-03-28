N = int(input())
li1 = list(map(int, input().split()))
li2 = sorted(set(li1))
dic = dict() # O(1) for getting values by keys

for i in range(len(li2)):
    dic[li2[i]] = i

for i in li1:
    print(dic[i], end=' ')