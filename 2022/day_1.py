# -----------------day 1-----------------
import re
file = open("adv.txt", "r")
el = 0
elf_sum_list=[]
sum_list = []
for line in file:
    # print (line)
    if line == '\n':
        elf_sum_list.append(sum(sum_list))
        sum_list = []
        # print (sum_list)
        # sum_list = []
        el += 1
    else:
        sum_list.append(int(line))

elf_sum_list.sort()
total_3 = elf_sum_list[-1] + elf_sum_list[-2] + elf_sum_list[-3]
print (f"Total No of Elf:{el} \n {elf_sum_list[-1]} \n {total_3}")

