
def twopointer(nums: int, target: int, n_list: list):
    n_list.sort()
    left, right = 0, nums - 1
    cnt = 0
    while left < right:
        if n_list[left] + n_list[right] == target:
            cnt += 1
        if n_list[left] + n_list[right] < target:
            left += 1
            continue
        right -= 1
    print(cnt)

n = int(input())
n_list = list(map(int, input().split()))
x = int(input())

twopointer(n, x, n_list)
