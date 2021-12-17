def stars(N):
    arr = []
    for i in range(3 * len(N)):
        if i // len(N) == 1:
            arr.append(N[i % len(N)] + ' ' * len(N) + N[i % len(N)])
        else:
            arr.append(N[i % len(N)] * 3)
    return(arr)

star = ['***', '* *', '***']
N = int(input())
k = 0
while N != 3:
    N = int(N  / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)
# 미완
# 이건 진짜 나중에 다시 풀던가 물어보던가하자..ㅠㅠㅠㅠㅠ
       
