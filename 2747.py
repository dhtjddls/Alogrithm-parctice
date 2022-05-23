n = int(input())
dyli = [0] * (n+1)
dyli[0], dyli[1] = 0, 1
for i in range(2, n+1):
    dyli[i] = dyli[i-2] + dyli[i-1]

print(dyli[n])