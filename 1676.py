n = int(input())
score = 1
for i in range(1, n+1):
    score *= i

cnt = 0
score = list(str(score))

for i in score[::-1]:

    if i != '0':
        break
    cnt += 1
    
print(cnt)