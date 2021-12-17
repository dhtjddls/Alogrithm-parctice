N = int(input())
result = 0
for i in range(1, N+1):
    A = list(map(int, str(i)))
    result = i + sum(A)
    if result == N:
        print(i)
        break
    if i == N:
        print(0)

# 1부터 해당 번호까지 모두 검색하면서 생성자를 찾아내는 문제 나는 뭐든 구현이 힘들더라..ㅠㅠㅠ 여튼 잡기술로 문자열을 맵함수로 정수화 시켜주면 각 자릿수 요소 하나하나씩 변환이 되기 때문에 맵함수를 이용해서 문제를 푸는 방법이었다.