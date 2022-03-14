# link: https://leetcode.com/problems/number-of-enclaves/

# idea 
# if land cells were totally surrounded by sea cells, add counts to the result
# conversly, if lands were on the edge, we don't count -> clean these cells
# use dfs to search through the cells
def enclaves(grid):
    dirs = [[0,1], [0,-1], [1,0], [-1,0]]

    def search(i, j):
        # mark visited
        grid[i][j] = 0
        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1: 
                search(i,j)

    for i in range(len(grid)):
        for j in range(len(grid[0])): 
            if grid[i][j] == 1 and (i == 0 or j == 0 or i == len(grid) or j == len(grid[0])):
                search(i,j)
    
    return sum(sum(grid,[]))
 
cells = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(enclaves(cells))

