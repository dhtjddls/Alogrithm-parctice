N = int(input())
user_list = []
for i in range(N):
    x, y = map(int, input().split())
    user_list.append((x, y))

for i in user_list:
    k = 1
    for j in user_list:
        if i[0] < j[0] and i[1] < j[1]:
            k += 1
    print(k, end=' ')


# 2중 for문을 통한 브루트 포스 

    
