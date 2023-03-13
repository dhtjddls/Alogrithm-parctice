import sys

input = sys.stdin.readline

# 20 + 40 - 60 + 25 + 66 - 30 + 100
# - 뒤에는 다더해야되 다음 - 전까지 
# - 기준으로 split 해주고 -> 대총 콘솔 찍으면서 연산해주면 될거같은데용

sik = input()
#1. 마이너스 기준으로 스플릿한다
result=sik.split('-')
#['55+30' / '50+40', '40', '40+50']

fin=sum(list(map(int, result[0].split('+'))))
for i in range(1,len(result)): 
    fin -= sum(list(map(int, result[i].split('+'))))

print(fin)
