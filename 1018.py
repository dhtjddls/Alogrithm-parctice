n, m = map(int, input().split())
chess_list = list()
cnt = list()

for _ in range(n):
    chess_list.append(input())

for i in range(n-7):
    for j in range(m-7):
        index1 = 0
        index2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if chess_list[a][b] != 'W':
                        index1 += 1
                    if chess_list[a][b] != 'B':
                        index2 += 1
                else:
                    if chess_list[a][b] != 'B':
                        index1 += 1
                    if chess_list[a][b] != 'W':
                        index2 += 1
        cnt.append(min(index1, index2))
        

print(min(cnt))
