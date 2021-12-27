n = int(input()) # 도시 개수 입력
dis = list(map(int, input().split())) # 거리 입력
cost = list(map(int, input().split())) # 리터당 가격 입력

cnt = 0 # 가격 저장 변수 설정
min_cost = cost[0] # 시작점을 최소 코스트로 일단 설정

for i in range(n-1): # 코스트의 마지막 부분은 필요 없으니 n-1 까지만 순회
    if cost[i] < min_cost: # 순회하다 더 작은 코스트를 발견하면
        min_cost = cost[i] # 더 작은 코스트로 갱신
    cnt += dis[i] * min_cost # 지금 까지 중 제일 적은 코스트니까 다음 거리만큼 주유해주고 카운트에 더해주기
print(cnt) # 결국 제일 적은 코스트일때 제일 많이 주유하기 때문에 최소값

# 결국 코스트의 마지막 부분을 제외하고 가장 작은 값일 때 가장 많이 주유하면 되는 그리디 문제.

