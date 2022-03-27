S = input()
cnt = 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        cnt += 1
if cnt % 2 == 0:
    print(cnt // 2)
else:
    print(cnt // 2 + 1)
