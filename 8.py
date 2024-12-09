"""
Part 1

"""

grid = [] 
with open("8input.txt", "r") as myfile:
    for line in myfile:
        grid.append(list(line.strip()))

# get matrix dimensions
cols, rows = len(grid[0]), len(grid)

# bounds check
def in_bound(r, c):
    return r in range(rows) and c in range(cols)

def print_grid():
    for row in grid:
        print("".join(row))

print_grid()
print(rows, cols)

# iterate over grid to find unique antennas
ant = dict()
for r in range(rows):
    for c in range(cols):
        ch = grid[r][c]
        if ch != '.':
            if ch not in ant: ant[ch] = [(r, c)]
            else: ant.get(ch).append((r, c))

print(ant)

# oterate over each pair and find antinodes
antinodes = set()
for nodes in ant.values():
    for a in nodes:
        for b in nodes:
            if a == b: continue
            x = a[0] + a[0] - b[0]
            y = a[1] + a[1] - b[1]
            if (in_bound(x, y)): antinodes.add((x, y))

print(len(antinodes))

"""
Part 2
"""
# oterate over each pair and find antinodes
antinodes = set()
for nodes in ant.values():
    for a in nodes:
        antinodes.add(a)
        for b in nodes:
            if a == b: continue
            for brute_force in range(1, 1000):
                x = a[0] + (a[0] - b[0]) * brute_force
                y = a[1] + (a[1] - b[1]) * brute_force
                if (in_bound(x, y)): antinodes.add((x, y))

print(len(antinodes))