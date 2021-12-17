import sys
n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
t.sort()
#print(t)
if n % 2 == 0:
    M = 0
    for i in range(n//2):
        M = max(t[i]+t[n-i-1], M)
        #print(i)
else:
    M = t[n-1]
    for i in range(n // 2):
        M = max(t[i] + t[n - i - 2], M)
        #print(i)
print(M)