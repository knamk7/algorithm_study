# 못 푼 문제

candidates = set()

for i in range(123, 988):
    i = str(i)
    if '0' in i:
        continue
    elif i[0]==i[1] or i[0]==i[2] or i[1]==i[2]:
        continue
    else:
        candidates.add(i)
temp = candidates

# for i in range(1,10):
#     for j in range(1,10):
#         if j != i:
#             for k in range(1,10):
#                 if k != i and k != j:
#                     candidates.add()


N = int(input())
answers = list()

for i in range(N):
    answers.append(input().split())

numbers = {'1','2','3','4','5','6','7','8','9'}
''''''
for i in answers:
    if i[1] == '3':                     #3S
        candidates = {i[0]}
        break
    
    elif i[1] == '2':                   #2S
        temp0 = numbers
        for j in i[0]:
            temp0.discard(j)
        for j in temp0:
            for k in candidates:
                if (i[0][0]+i[0][1]+j) == k:
                    pass
                elif (i[0][0]+j+i[0][2]) == k:
                    pass
                elif (j+i[0][1]+i[0][2]) == k:
                    pass
                else:
                    temp.discard(k)
        candidates = temp
    
    elif i[1] == '1':
        if i[2] == '2':                 #1S2B
            numbers = set(i[0])
            candidates = candidates & {i[0][0]+i[0][2]+i[0][1], i[0][2]+i[0][1]+i[0][0], i[0][1]+i[0][0]+i[0][2]}
        elif i[2] == '1':               #1S1B
            temp0 = numbers
            for j in i[0]:
                temp0.discard(j)
            for j in temp0:
                for k in candidates:
                    if (i[0][0]+j+i[0][1]) == k:
                        pass
                    elif (i[0][0]+i[0][2]+j) == k:
                        pass
                    elif (j+i[0][1]+i[0][0]) == k:
                        pass
                    elif (i[0][2]+i[0][1]+j) == k:
                        pass
                    elif (j+i[0][0]+i[0][2]) == k:
                        pass
                    elif (i[0][1]+j+i[0][2]) == k:
                        pass
                    else:
                        temp.discard(k)

        else:                           #1S
            temp0 = numbers
            for j in i[0]:
                temp0.discard(j)
            for j in temp0:
                temp0.discard(j)
                for k in temp0:
                    for l in candidates:
                        if (i[0][0]+j+k) == l:
                            pass
                        elif (i[0][0]+k+j) == l:
                            pass
                        elif (j+i[0][1]+k) == l:
                            pass
                        elif (k+i[0][1]+j) == l:
                            pass
                        elif (k+j+i[0][2]) == l:
                            pass
                        elif (j+k+i[0][2]) == l:
                            pass
                        else:
                            temp.discard(l)
        candidates = temp

    elif i[1] == '0':
        if i[2] == '3':                 #3B
            numbers = set(i[0])
            candidates = candidates & {i[0][1]+i[0][2]+i[0][0], i[0][2]+i[0][0]+i[0][1]}
        elif i[2] == '2':               #2B
            temp0 = numbers
            temp1 = set()
            if j in i[0]:
                temp0.discard(j)
            for j in temp0:
                temp1.update({j+i[0][0]+i[0][1], i[0][1]+j+i[0][0], j+i[0][2]+i[0][0], i[0][2]+i[0][0]+j, i[0][2]+j+i[0][1], i[0][1]+i[0][2]+j})
            candidates = candidates & temp1
        elif i[2] == '1':               #1B
            for j in candidates:
                if i[0][0] == j[0]:
                    temp.discard(j)
                elif i[0][1] == j[1]:
                    temp.discard(j)
                elif i[0][2] == j[2]:
                    temp.discard(j)
                elif i[0][0] in j:
                    if i[0][1] in j:
                        temp.discard(j)
                    elif i[0][2] in j:
                        temp.discard(j)
                elif i[0][1] in j:
                    if i[0][2] in j:
                        temp.discard(j)
        elif i[2] == '0':               #0B
            for j in i[0]:
                numbers.discard(j)
            for j in candidates:
                if i[0] in j or i[1] in j or i[2] in j:
                    temp.discard(j)
            candidates = temp

print(len(candidates))