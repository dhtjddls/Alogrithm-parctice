from collections import Counter
n = input()
n = list(n)

for i in range(len(n)):
    if n[i] == '6':
        n[i] = '9'


counter = Counter(n)
if "9" in counter:
    if counter['9'] % 2 == 0:
        counter['9'] = counter['9'] // 2
    else:
        counter['9'] = counter['9'] // 2 + 1
        
print(counter.most_common()[0][1])