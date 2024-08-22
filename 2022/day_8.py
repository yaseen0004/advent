import numpy as np

file = open("test.txt", "r")

forest =[]

for line in file:
    line = line.strip()
    forest.append(line)
    
length = len(forest[0])
width = len(forest)

total_outside_tree = (length * 2) + (width * 2) - 4
print("Total trees on edge =",total_outside_tree)

count = 0
for trees in forest:
    # top - edge
    if trees == forest[0]:
        count += len(trees)
        continue
    # bottom - edge
    elif trees == forest[-1]:
        count += len(trees)
        continue
    # from - right
    else:
        tallest = max(trees)
        for i in range(0,length):
            if tallest == trees[i]:
                count += 1
                break
            elif i == 0:
                continue
            elif trees[i] > trees[i-1]:
                count += 1

print(count)