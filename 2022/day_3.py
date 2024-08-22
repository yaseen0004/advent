import string
import textwrap
from collections import Counter


file = open("adv.txt", "r")

alphabet = list(string.ascii_letters)
alphabet_dict = {}
count = 1
for each in alphabet:
    alphabet_dict[each] = count
    count += 1

# part 1 ==================================
# sum_a = 0
# for line in file:
#     line = line.strip()
#     length = len(line)/2

#     split_line = textwrap.wrap(line, int(length))

#     dict1 = Counter(split_line[0])
#     dict2 = Counter(split_line[1])
#     commonDict = dict1 & dict2
#     commonChars = list(commonDict.elements())

#     sum_a = sum_a + alphabet_dict[commonChars[0]]

# print (sum_a)

# part 2 ==================================
sum_b = 0
line_count = 0
lines_list = []
for line in file:
    line = line.strip()
    lines_list.append(line)
    line_count += 1

    if line_count == 3:
        dict1 = Counter(lines_list[0])
        dict2 = Counter(lines_list[1])
        dict3 = Counter(lines_list[2])
        commonDict = dict1 & dict2 & dict3
        commonChars = list(commonDict.elements())
        sum_b = sum_b + alphabet_dict[commonChars[0]]

        line_count = 0
        lines_list = []

print (sum_b)
