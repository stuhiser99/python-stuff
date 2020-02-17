
# Conway's game of life

def nextCell(isalive, neighbors):
    if neighbors == 3:
        return True
    elif neighbors == 2:
        return isalive
    else:
        return False
        
def nextGrid(grid):
    newGrid = list()
    for r in range(len(grid)):
        newRow = list()
        for c in range(len(grid[r])):
            neigh = 0
            if r > 0:
                neigh += 1 if c>0 and grid[r-1][c-1] else 0
                neigh += 1 if grid[r-1][c] else 0
                neigh += 1 if c+1 < len(grid[r]) and grid[r-1][c+1] else 0
            neigh += 1 if c>0 and grid[r][c-1] else 0
            neigh += 1 if c+1 < len(grid[r]) and grid[r][c+1] else 0
            if r < len(grid[r])-1:
                neigh += 1 if c>0 and grid[r+1][c-1] else 0
                neigh += 1 if grid[r+1][c] else 0
                neigh += 1 if c+1 < len(grid[r]) and grid[r+1][c+1] else 0
            newCell = nextCell(grid[r][c], neigh)
            newRow.append(newCell)
        newGrid.append(newRow)
    return newGrid
    
def rowToString(row):
    pr = ['*' if l else '_' for l in row]
    return ' '.join(pr)

def printGrid(grid):
    for row in grid:
        print(rowToString(row))
        

# [ random.random() >0.75 for i in range(20)]

if __name__ == '__main__':
    # simple test case
    grid = list()
    for i in range(5):
        grid.append( [False for j in range(5)] )
    grid[2][1] = True
    grid[2][2] = True
    grid[2][3] = True
    
    printGrid(grid)
    next = nextGrid(grid)
    printGrid(next)
    