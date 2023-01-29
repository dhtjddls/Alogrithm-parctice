score_arr = list()
idx_arr = list()
for _ in range(8):
    score = int(input())
    score_arr.append(score)
    idx_arr.append(score)
score_arr.sort(reverse=True)
total = score_arr[:5]
print(sum(total))
total_idx = list()
for i in total:
    total_idx.append(idx_arr.index(i)+1)
for i in sorted(total_idx):
    print(i, end=' ')

