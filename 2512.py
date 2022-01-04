
n, m = map(int,input().split())
n_list = list(int(input()) for _ in range(n))
m_list = list(int(input()) for _ in range(m))
cnt = 0
input()
for i in n_list:
    start = 0
    end = len(m_list)
    while start <= end:
        mid = (start + end) // 2
        if i == m_list[mid]:
            cnt += 1
            break
        elif i > m_list[mid]:
            start = mid + 1
        else:
            end = mid - 1

print(cnt)
