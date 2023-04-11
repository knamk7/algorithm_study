N = int(input())
numbers = []
for i0 in range(10):
    numbers.append(i0)
    for i1 in range(i0):
        numbers.append(int(str(i0)+str(i1)))
        for i2 in range(i1):
            numbers.append(int(str(i0)+str(i1)+str(i2)))
            for i3 in range(i2):
                numbers.append(int(str(i0)+str(i1)+str(i2)+str(i3)))
                for i4 in range(i3):
                    numbers.append(int(str(i0)+str(i1)+str(i2)+str(i3)+str(i4)))
                    for i5 in range(i4):
                        numbers.append(int(str(i0)+str(i1)+str(i2)+str(i3)+str(i4)+str(i5)))
                        for i6 in range(i5):
                            numbers.append(int(str(i0)+str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)))
                            for i7 in range(i6):
                                numbers.append(int(str(i0)+str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)))
                                for i8 in range(i7):
                                    numbers.append(int(str(i0)+str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)))
                                    for i9 in range(i8):
                                        numbers.append(int(str(i0)+str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)))      
numbers.sort()
if N < len(numbers):
    print(numbers[N])
else:
    print(-1)