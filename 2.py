"""
Part 1
Read through the file line by line.
Set up two functions to check for the two conditions.
Filter each row through both functions, increment if both pass.
"""

def check_mono (row):
    length = len(row)
    count = 0
    
    for i in range(length - 1):
        if (int(row[i]) < int(row[i + 1])):
            count -= 1
        else:
            count += 1
    return (abs(count) == length - 1)

def check_diff (row):
    length = len(row)
    count = 0
    
    for i in range(length - 1):
        if abs(int(row[i]) - int(row[i + 1])) in [1, 2, 3]:
            count += 1
    return (count == length - 1)

safe = 0
rows = []
with open("2input.txt", "r") as myfile:
    for line in myfile:
        row = line.strip().split()
        rows.append(row) 

for row in rows:
    if check_mono(row) and check_diff(row):
            safe += 1 

print(safe)

"""
Part 2
Brute force. To refactor later...
"""
safe = 0

for row in rows:
    for idx in range(len(row)):
        subrow = [element for i, element in enumerate(row) if i != idx]
        if check_mono(subrow) and check_diff(subrow):
            safe += 1
            break

print(safe)