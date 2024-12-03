"""
Part 1
Read file in single line.
Use regex matching to extract all instances of mul(x,y) into list.
Split on ',' and slice out the unecessary chars.
Cast to int, multiply, sum list.
"""

import re;

line = open("3input.txt", "r").read()

a = re.findall( r"mul\(\d+,\d+\)", line)
print(sum([int(i.split(',')[0][4:]) * int(i.split(',')[1][:-1]) for i in a]))

"""
Part 2
Update regex to also find do() and don't().
Iterate sequentially through, updating a running total (sum) when a flag (do) is 1.
Start with do = 1 to accept first mul(x,y).
"""

a = re.findall( r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

sum = 0
do = 1
for item in a:
    if item[0] == "m": # it's a mul instruction
        if do == 1: 
            sum += int(item.split(',')[0][4:]) * int(item.split(',')[1][:-1])
    elif item == "do()": # set flag to do next mul
        do = 1
    elif item == "don't()": # set flag to skip next mul
        do = 0
    else:
        raise Exception() # should never get here
print(sum)