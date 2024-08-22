import re


file = open("adv.txt", "r")

count = 0

for line in file:
    line = line.strip()

    temp = re.findall(r'\d+', line)
    res = list(map(int, temp))

#     # first inside second
#     if res[0] >= res[2] and res[1] <= res[3]:
#         count += 1
#         print (res)
#     # second inside first
#     elif res[0] <= res[2] and res[1] >= res[3]:
#         print (res)
#         count += 1

# print(count)

# part2===============================

    a_list = list(range(res[0], res[1]+1))
    b_list = list(range(res[2], res[3]+1))
    c_list = [value for value in a_list if value in b_list]
    print(a_list)
    print(b_list)
    print(c_list)
    if c_list:
        count += 1


print(count)
