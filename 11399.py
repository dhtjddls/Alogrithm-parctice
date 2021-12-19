n = int(input())
atm = list(map(int, input().split()))
atm.sort()

cnt = 0
for i in range(len(atm)):
    cnt += atm[i] * (len(atm)-i)

print(cnt)

# 가장 작은 순서대로 배치해서 전체 구간합을 구하면 되는 그리디 문제였는데, 구간합을 구하는 과정에서 for문 2개를 쓸 필요없이 투포인터를 사용해 해결했다. 뿌듯했다.