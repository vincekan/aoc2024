"""
Part 1

"""

WALKED = 'X'
FREE = '.'

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

grid = [] 
with open("6input.txt", "r") as myfile:
    for line in myfile:
        grid.append(list(line.strip()))

# get matrix dimensions
max_x, max_y = len(grid[0]), len(grid)

# bounds check
def in_bound(j, i):
    return i in range(max_x) and j in range(max_y)

# checker func
def check(j, i, char):
    return True if grid[i][j] == char else False

# find guard
def find_guard():
    for x in range(max_x):
        for y in range(max_y):
            if check(x, y, UP): return [x, y, UP]
            if check(x, y, DOWN): return [x, y, DOWN]
            if check(x, y, LEFT): return [x, y, LEFT]
            if check(x, y, RIGHT): return [x, y, RIGHT]

def front_clear(guard):
    if guard[2] == UP and in_bound(guard[0], guard[1] - 1): 
        if check(guard[0], guard[1] - 1, '#'): return False
    if guard[2] == DOWN and in_bound(guard[0], guard[1] + 1): 
        if check(guard[0], guard[1] + 1, '#'): return False
    if guard[2] == LEFT and in_bound(guard[0] - 1, guard[1]): 
        if check(guard[0] - 1, guard[1], '#'): return False
    if guard[2] == RIGHT and in_bound(guard[0] + 1, guard[1]): 
        if check(guard[0] + 1, guard[1], '#'): return False
    return True

def turn_guard(guard):
    if guard[2] == UP: return RIGHT
    if guard[2] == DOWN: return LEFT
    if guard[2] == LEFT: return UP
    if guard[2] == RIGHT: return DOWN

def move_guard(guard):
    while(not front_clear(guard)):
        guard[2] = turn_guard(guard)
    
    if guard[2] == UP: guard[1] -= 1
    if guard[2] == DOWN: guard[1] += 1
    if guard[2] == LEFT: guard[0] -= 1
    if guard[2] == RIGHT: guard[0] += 1

    return (guard)

    
def update_walked(j, i):
    grid[i][j] = WALKED
    
def print_grid():
    for row in grid:
        print("".join(row))

# guard starting position
guard = find_guard()

# loop
while(in_bound(guard[0], guard[1])):
    update_walked(guard[0], guard[1])
    guard = move_guard(guard)
    #print_grid()

print(sum(row.count('X') for row in grid))

"""
Part 2
Brute force
"""

count = 0
for x in range(max_x):
    for y in range(max_y):
        print(f'x, y: {x}, {y}, count = {count}')
        grid = [] 
        with open("6input.txt", "r") as myfile:
            for line in myfile:
                grid.append(list(line.strip()))

        # make new grid - this happens one for each empty tile
        if grid[x][y] == FREE:
            grid[x][y] = '#'
            
            # guard starting position
            guard = find_guard()
            # loop - copied form p1
            ctr = 0
            while(in_bound(guard[0], guard[1]) and ctr < 100000):
                ctr += 1
                update_walked(guard[0], guard[1])
                guard = move_guard(guard)
                #print_grid()
            if ctr == 100000:
                #timed out
                count += 1
            else:
                pass

print(count)