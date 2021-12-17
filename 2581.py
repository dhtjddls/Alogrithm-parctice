import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prime_list = []
for i in range(M, N + 1):
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 0:
        prime_list.append(i)

if len(prime_list) < 1:
    print('-1')
else:
    print(sum(prime_list))
    print(min(prime_list))

# 솔직히 좀 쉬울 것 같았는데 시간초과가 나서 얕봤다 하고 한참 고생한 문제다. 기본 구조는 그냥 소수 판별문제랑 비슷하다. 지정된 수가 있고 0, 1로 나누는 건 의미가 없으니까 2부터 해당 수 -1 까지 나눠주면서 소수를 판별한다. 하지만 시간 초과가 났고 input을 sys.stdin.readline으로 바꿔주고 판별범위를 가운데 지점으로 바꿔 mid = i // 2 이런 식으로 절반으로 줄여보기도 했지만 번번히 실패했다. 그러나 해답은 cnt가 일정 갯수를 초과하면 바로 넘어가는 식으로 시간초과를 해결할 수 있었다. 11~12번 줄!