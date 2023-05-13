def fibonacci(n):
    f = [0,1,1]
    for i in range(3, n+1):
        f.append(f[-1] + f[-2])
    return f[-1]

n = int(input())

print(fibonacci(n), n-2)


# Another Solution O(1)
'''
import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (1-phi)**n) / math.sqrt(5))

n = int(input())

print(fibonacci(n), n-2)
'''