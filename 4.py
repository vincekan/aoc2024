"""
Part 1
Find each X position in the grid and check every direction
Increment by hits found
Uses truthy python values 
"""

# hardcoded bound from main file...
bounds = range(0, 140)

def h(i, j):
    j += 3
    # check j doesnt exceed bounds first, then slice out the next three chars to find XMAS
    return (j in bounds and ''.join(grid[i][j - 2: j + 1]) == 'MAS')

def h2(i, j):
    j -= 3
    return (j in bounds and ''.join(grid[i][j: j + 3]) == 'SAM')     

def v(i, j):
    i += 3
    return (i in bounds and ''.join(grid[i - 2][j]+ grid[i - 1][j]+ grid[i][j]) == 'MAS')

def v2(i, j):
    i -= 3
    return (i in bounds and ''.join(grid[i][j]+ grid[i + 1][j]+ grid[i + 2][j]) == 'SAM')

def d1(i, j):
    i += 3
    j += 3
    if i in bounds and j in bounds:
        return ''.join(grid[i - 2][j - 2]+ grid[i - 1][j - 1]+ grid[i][j]) == 'MAS'
    return 0

def d2(i, j):
    i -= 3
    j += 3
    if i in bounds and j in bounds:
        return ''.join(grid[i + 2][j - 2]+ grid[i + 1][j - 1]+ grid[i][j]) == 'MAS'
    return 0

def d3(i, j):
    i -= 3
    j -= 3
    if i in bounds and j in bounds:
        return ''.join(grid[i + 2][j + 2]+ grid[i + 1][j + 1]+ grid[i][j]) == 'MAS'
    return 0

def d4(i, j):
    i += 3
    j -= 3
    if i in bounds and j in bounds:
        return ''.join(grid[i - 2][j + 2]+ grid[i - 1][j + 1]+ grid[i][j]) == 'MAS'
    return 0

grid = [] 
with open("4input.txt", "r") as myfile:
    for line in myfile:
        grid.append(list([ch for ch in (line.strip())]))    # list of list = 140 * 140

count = 0
for j, col in enumerate(grid):
    for i, row in enumerate(col):
        if grid[i][j] == 'X':
            count += h(i, j) + h2(i, j) + v(i, j) + v2(i, j)
            count += d1(i, j) + d2(i, j) + d3(i, j) + d4(i, j)

print(count) 

"""
Part 2
Add diagonal checking functions
"""
def d(i, j):
    # define the four corners
    a = i + 1
    b = j + 1
    c = i - 1
    d = j - 1
    # check all in bound
    if a in bounds and b in bounds and c in bounds and d in bounds:
        # check if they are in a valid arrangement
        return (''.join(grid[a][b] + grid[a][d] + grid[c][d] + grid[c][b]) in ['SSMM', 'SMMS', 'MMSS', 'MSSM'])
    return 0

count = 0
for j, col in enumerate(grid):
    for i, row in enumerate(col):
        if grid[i][j] == 'A':
            count += d(i, j)

print(count) 