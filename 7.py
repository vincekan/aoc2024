"""
Part 1

"""

data = [] 
with open("7input.txt", "r") as myfile:
    for line in myfile:
        data.append(line.strip().split(':'))

sums = [int(d[0]) for d in data]
nums = [[int(x) for x in d[1].split()] for d in data]

print(sums)
print(nums)

def check(sum: int, nums: list, total: int) -> bool:
    if len(nums) == 0: return False # no more values to add or mult
    else:
        next = nums.pop(0)
        nums2 = nums.copy() # make a new list... inefficient but stops double popping
        if (total * next == sum or total + next == sum) and len(nums) == 0: return True
        else: return (check(sum, nums, total * next) or check(sum, nums2, total + next))

total = 0
for i in range(len(data)):
    if check(sums[i], nums[i][1:], nums[i][0]): total += sums[i]

print(total)

"""
Part 2
"""
def check2(sum: int, nums: list, total: int) -> bool:
    if len(nums) == 0: return False # no more values to add or mult
    else:
        next = nums.pop(0)
        nums2 = nums.copy() # make a new list... inefficient but stops double popping
        nums3 = nums.copy() # make a new list... inefficient but stops double popping
        concat = int(str(total) + str(next))
        if (total * next == sum or total + next == sum or concat == sum) and len(nums) == 0: return True
        else: return (check2(sum, nums, total * next) 
                    or check2(sum, nums2, total + next)
                    or check2(sum, nums3, concat))

total = 0
for i in range(len(data)):
    if check2(sums[i], nums[i][1:], nums[i][0]): total += sums[i]

print(total)