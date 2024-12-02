"""
Part 1
Read through the file line by line.
Add to two lists and cast.
Sort lists (probably inefficient, O(nlogn) - maybe there is a way to avoid sorting).
Iterate through and sum absolute values.
"""

safe = 0

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

with open("2input.txt", "r") as myfile:
    for line in myfile:
        row = line.strip().split()

        if check_mono(row) and check_diff(row):
            safe += 1 

    print(safe)

"""
Part 2
Brute force. To refactor later...
"""
safe = 0
rows = []
with open("2input.txt", "r") as myfile:
    for line in myfile:
        row = line.strip().split()
        rows.append(row)

for row in rows:
    print(row)
    for idx in range(len(row)):
        subrow = [element for i, element in enumerate(row) if i != idx]
        
        print(subrow, check_mono(subrow),  check_diff(subrow))
        if check_mono(subrow) and check_diff(subrow):
            safe += 1
            break

print(safe)