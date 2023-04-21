a = input().split('-')
result = sum(map(int, a[0].split('+')))
for i in a[1:]:
    result -= sum(map(int, i.split('+')))
print(result)