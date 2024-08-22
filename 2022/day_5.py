import string
import re

def get_key(val):
    for key, value in alphabet_dict.items():
        if val == value:
            return key

file = open("adv.txt", "r")

# main_dict ={
#     "a" : ['Z','N'],
#     "b" : ['M','C','D'],
#     "c" : ['P']
# }

main_dict ={
    "a" : ['F','H','B','V','R','Q','D','P'],
    "b" : ['L','D','Z','Q','W','V'],
    "c" : ['H','L','Z','Q','G','R','P','C'],
    "d" : ['R','D','H','F','J','V','B'],
    "e" : ['Z','W','L','C'],
    "f" : ['J','R','P','N','T','G','V','M'],
    "g" : ['J','R','L','V','M','B','S'],
    "h" : ['D','P','J'],
    "i" : ['D','C','N','W','V'],
}

alphabet = list(string.ascii_letters)
alphabet_dict = {}
count = 1
for each in alphabet:
    alphabet_dict[each] = count
    count += 1

# for line in file:
#     line = line.strip()

#     temp = re.findall(r'\d+', line)
#     res = list(map(int, temp))
    
#     from_stack = get_key(res[1])
#     to_stack = get_key(res[2])

#     for i in range(0,res[0]):
#         val = main_dict[from_stack].pop()
#         main_dict[to_stack].append(val)

# final_string = ""
# for each in main_dict:
#     final_string += main_dict[each][-1]
# print(final_string)

# part 2 =======================================

for line in file:
    line = line.strip()

    temp = re.findall(r'\d+', line)
    res = list(map(int, temp))
    
    from_stack = get_key(res[1])
    to_stack = get_key(res[2])

    temp_list = []
    for i in range(0,res[0]):
        temp_val = main_dict[from_stack].pop()
        temp_list.append(temp_val)
    print(temp_list)
    for each in reversed(temp_list):
        main_dict[to_stack].append(each)

    print(main_dict)
    
final_string = ""
for each in main_dict:
    if main_dict[each]:
        final_string += main_dict[each][-1]
print(final_string)