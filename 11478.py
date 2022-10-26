s = input()
s_rlt = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j+1]
        s_rlt.add(temp)

print(len(s_rlt))
