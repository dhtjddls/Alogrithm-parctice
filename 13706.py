def binary_search(s, e):
    target = e
    while True:
        mid = (s + e) // 2
        if (mid ** 2) == target:
            return mid
        if mid ** 2 > target:
            e = mid
        elif mid ** 2 < target:
            s = mid

N = int(input())
print(binary_search(1, N))

# 이것도 이분 탐색 기본! 숫자는 이미 정렬되어있으니가 숫자 받아서 제곱근이 나올 때 까지 이분탐색!
