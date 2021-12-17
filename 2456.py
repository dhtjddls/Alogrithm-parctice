N = int(input())
a = 0
b = 0
c = 0
for i in range(N):
    z = list(map(int, input().split()))
    a += z[0]
    b += z[1]
    c += z[2]
total = [a, b, c]
if total.count(max(total)) > 1:
    print(0, max(total))
else:
    print(total.index(max(total)) + 1, max(total))

#미완
