n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))

# 어 수학을 몰라서 못푼 문제. 30의 배수가 되기 위해서는 일단 맨뒤가 0으로 시작해야한다는 것 까지는 캐치 가능 근데?! 모든 자릿수의 합이 3의 배수가 되어야 가능하다는 것은 캐치 불가했다. 이 두개가 만족 됐을때, 가장큰 30의 배수이기 때문에 내림차순으로 정리한 거를 그대~로 합쳐서 출력해주면 최대가 된다.