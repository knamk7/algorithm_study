n = int(input()) % 47244 # Pisano Period from https://moon323.tistory.com/22

f = [1,1,2]
for i in range(n-1):
    f[2] = ((f[1]+f[0]) % 15746)
    f[0] = f[1]
    f[1] = f[2]

print((f[1]))