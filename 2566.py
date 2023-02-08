grid = []
for i in range(9):
   grid.append(list(map(int, input().split())))

max_val = 0
max_x = 0
max_y = 0 
for i in range(9):
    for j in range(9):
        if max_val < grid[i][j]:
            max_val = grid[i][j]
            max_x = i
            max_y = j

print(max_val)
print(max_x+1, max_y+1)