"""
Part 1
Read through the file line by line.
Add to two lists and cast.
Sort lists (probably inefficient, O(nlogn) - maybe there is a way to avoid sorting).
Iterate through and sum absolute values.
"""

sums = 0
A = list()
B = list()

with open("1input.txt", "r") as myfile:
    for line in myfile:
        a, b = line.strip().split()
        A.append(int(a))
        B.append(int(b))

A.sort()
B.sort()
for a, b, in zip(A, B):
    sums += abs(a - b)
print(sums)

"""
Part 2
Inefficient nested loop. O(n2).
"""

sums = 0
for a in A:
    multiplier = 0
    for b in B:
        if a == b:
            multiplier += 1
    sums += a * multiplier
    #print(a, len(B), multiplier, sums)
print(sums)