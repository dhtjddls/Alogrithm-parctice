prime_list = [False, False] + [True] * 60000
for i in range(2, int(pow(10000, 0.5) + 1)):
    if prime_list[i] == True:
        for j in range(2 * i, len(prime_list), i):
            prime_list[j] = False

T = int(input())
for _ in range(T):
    n = int(input())
    mid_up = n // 2
    mid_down = mid_up
    for _ in range(len(prime_list)):
        if prime_list[mid_up] and prime_list[mid_down]:
            print(mid_down, mid_up)
            break
        mid_up += 1
        mid_down -= 1


# 에라토스 테네스의 체를 쬐금은 이해할 수 있던 문제였다. 처음부터 전체범위에서 소수 판별리스트를 만든후에 주어진 값의 가운데 값에서 대조하는 값의 인덱스를 하나는 증가하고 하나는 감소하게 해서 맞아떨어질 때 판별하는 방법이다. 그러나 기본적으로 맞아 떨어질지 아닐지 고민하는게 아니라 무조건 맞아 떨어진다는 설명이 있기 때문에 가운데에서 모두 소수인 지점을 그대로 출력하면 된다. 소수를 판별할 때는 가능하면 꼭 해당 범위의 제곱근 값내의 모든 소수의 배수를 지우면 소수만 남게된다는 에라토스 테네스의 체를 기억하자!