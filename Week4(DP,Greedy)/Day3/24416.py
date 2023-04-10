# 미완성
count = 0

def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_dp(n):
    count = 0
    f = [0,1,1]
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return count

n = int(input())

print(count_recur, fib_dp(n))