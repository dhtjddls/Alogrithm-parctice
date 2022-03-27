n = int(input())
rope = [int(input()) for i in range(n)]
value = []
rope.sort(reverse=True)

for i in range(n):
    value.append(rope[i]*(i+1))

print(max(value))

# [20, 30, 40, 50] 이 있다고 해보자
# 로프가 1개 일때는 가장 큰 50
# 2개 일때는 2번째로 큰 40과 50이 40을 견디니까 40*2로 80
# 3개 일때는 30 *3 해서 90 이런식으로 결국 최대값은 정렬했을때
# n번째로 큰녀석 * n 을 해주면 되는 식이다.
