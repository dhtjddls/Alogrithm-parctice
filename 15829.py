L = int(input())
string = input()
answer = 0

for i in range(L):
    answer += (ord(string[i])-96) * (31 ** i) #아스키 코드 값을 돌려주는 ord함수
print(answer % 1234567891)

# 문제 이해가 난해한 문제. 그러나 각 글자를 아스키코드로 변환해서 각 문자별로 번호를 지정해주고 (96을 빼서 a가 1부터 시작할 수 있게 설정해주고) 제시된 조건대로 제곱과 나누기 등등을 해주면 되는 문제.
