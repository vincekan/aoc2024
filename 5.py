"""
Part 1

"""

lines = open("5input.txt", "r").readlines()

rules = [list(map(int,l.strip().split('|'))) for l in lines if len(l.strip().split('|')) == 2]
updates = [list(map(int,l.strip().split(','))) for l in lines if len(l.strip().split(',')) > 2]

# make dict of rules by page
ruleset = dict()
for r in rules:

    # If the key exists, add to the set
    if r[0] in ruleset:
        ruleset[r[0]].add(r[1])
    # If the key does not exist, create a new set
    else:
        ruleset[r[0]] = {r[1]}

# iterate through updates and check against ruleset
count = 0
wrong_order = []
for u in updates:
    flag = 0
    for i, v in enumerate(u):
        this_ruleset = ruleset.get(v)
        if this_ruleset == None:
            continue
        else:
            for this_rule in this_ruleset:
                if this_rule in u[:i]:
                    flag = 1 # broke rule

    if not flag: 
        count += u[int(len(u)/2)]
    else:
        wrong_order.append(u)
print(count)

"""
Part 2

"""
#wrong_order = wrong_order[-1:]
print(wrong_order)
count = 0
hmap = dict()
# reorder by most rules to least rules

for u in wrong_order:
    hmap = dict()
    iset = dict()
    clashset = set()
    for v in u:
        pages_after_v = sorted(ruleset.get(v), reverse = True)
        print(v, pages_after_v)
        for i in pages_after_v:
            # If the key exists, add to the set
            if i in iset and i in u:
                iset[i] += 1
            # If the key does not exist, create a new set
            elif i in u:
                iset[i] = 1
        #print(sorted(iset.keys()))
    for v in u:
        if v not in iset:
            iset[v] = 0

    print('iset: ', sorted((iset.keys())), sorted(iset.values()))
    for key in iset.keys():
        if iset.get(key) == min(iset.values()):
            print('key: ', key)
            clashset.add(key)
    bigclashset = set()
    
    fixed = []
    i = 0
    length = len(u) - 1
    while (i < length):
        for item in iset:
            if iset.get(item) == i: 
                fixed.append(item)
                i += 1
    print('fixed: ', fixed)
    print(fixed[int(len(fixed)/2)])
    count += fixed[int(len(fixed)/2)]

print(count)