N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
coin.reverse()
cnt = 0
for j in coin:
    cnt += (K // j)
    K %= j
print(cnt)

"""오.. 좀 쉬운데?ㅋㅋㅋㅋ내림차순으로 코인 리스트를 받아서
리스트를 반복문으로 대입하면서 몫을 카운트에 적립해주고
나머지를 k값으로 계속 대입해주면 끝! 그리디 알고리즘인 만큼
매번 가장 큰 값을 최대 몫으로 나누기를 반복하면 해결할 수 있는 문제이다."""