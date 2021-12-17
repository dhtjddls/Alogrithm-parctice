# 1. 그냥 시간 복잡도 O(n^2)의 풀이 리스트를 전부다 돌면서 탐색한다. 
"""
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

cnt_list = []
for i in m_list:
    cnt = 0
    for j in n_list:
        if i == j:
            cnt += 1
    cnt_list.append(cnt)

for i in cnt_list:
    print(i, end=' ')
"""
# 2. 해싱(딕셔너리)를 활용한 방법 
# 존재 유무를 판단한 후에 중복을 어떻게 해결하나 고민하다가 중복값을 먼저 딕셔너리에 저장해두고 찾을 때 호출만 하자. 딕셔너리를 저장하는 과정에서 원래는 count함수를 썻었는데 그러면 저장할 때 발견할때마다 n_list를 통짜로 계속 돌아야 해서 그러지말고 반복문으로 한번만 돌았더니 맞았다.

# (하나의 숫자를 찾으면 탐색리스트에서 제거하면 다음엔 더 빠르지 않을까? 라는 아이디어)

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))
dic = {}

for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in m_list:
    if j in dic:
        print(dic[j], end=' ')
    else:
        print('0', end=' ')

"""
    def binary(target, list):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid] == target:
                return list.count(target)
            elif list[mid] > target:
                end = mid - 1
            else: 
                start = mid + 1
        return 0
"""

