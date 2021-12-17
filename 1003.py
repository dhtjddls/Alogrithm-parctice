cnt0 = [1, 0] # 0의 디피 테이블
cnt1 = [0, 1] # 1의 디피 테이블

for i in range(2, 41):
    cnt0.append(cnt0[i-1] + cnt0[i-2])
    cnt1.append(cnt1[i-1] + cnt1[i-2])
# 전체를 먼저 메모장에 기록해 둡니다. 0의 호출회수 메모장, 1의 회수 메모장 후에는 해당 사항이 나오면 호출만 해주면 됩니다. 반복문으로 n번만 돌면 되죠 한번. 재귀적으로 돌면 매번 호출을 위에서 시작까지 해야해요.

test = int(input())
for _ in range(test):
    case = int(input())
    print(cnt0[case], cnt1[case])

