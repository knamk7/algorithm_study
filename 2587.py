a = list() # 저장할 배열 선언
sum = 0 # 평균 구할 때 저장할 용도

for i in range(5): # 5개 입력받기
    a.append(int(input()))
    sum = sum + a[i]

print(sum//5)
a.sort()
print(a[2])