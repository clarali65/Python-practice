def countServers(grid):
    row,col = len(grid),len(grid[0])
    crow=[0] * row
    ccol=[0] * col
    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                crow[i] = crow[i] + 1
                ccol[j] = ccol[j] + 1

    res = 0
    for i in range(row):
        for j in range(col):
            res = res + grid[i][j] and (crow[i] > 1 or ccol[j] > 1)
    return res

grid = eval(input())
print(countServers(grid))