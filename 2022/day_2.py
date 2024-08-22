# -----------------r1-----------------
# file = open("adv.txt", "r")
# total_points = 0
# for line in file:
#     game_point = 0
#     if line == '\n':
#         continue
#     else:
#         if line[0] == 'A' and line [2] =='X':
#             game_point = 4 # 3+1
#         elif line[0] == 'A' and line [2] =='Y':
#             game_point = 8 # 6+2
#         elif line[0] == 'A' and line [2] =='Z':
#             game_point = 3 # 0+3
#         elif line[0] == 'B' and line [2] =='X':
#             game_point = 1 # 0+1
#         elif line[0] == 'B' and line [2] =='Y':
#             game_point = 5 # 3+2
#         elif line[0] == 'B' and line [2] =='Z':
#             game_point = 9 # 6+3
#         elif line[0] == 'C' and line [2] =='X':
#             game_point = 7 # 6+1
#         elif line[0] == 'C' and line [2] =='Y':
#             game_point = 2 # 0+2
#         elif line[0] == 'C' and line [2] =='Z':
#             game_point = 6 # 3+3
#         total_points += game_point
        
# print (total_points)

# w = 6
# l = 0
# d = 3
# r = 1
# p = 2
# s = 3

# -----------------r2-----------------
file = open("adv.txt", "r")
total_points = 0
for line in file:
    game_point = 0
    if line == '\n':
        continue
    else:
        if line[0] == 'A' and line [2] =='X':
            game_point = 3+0
        elif line[0] == 'A' and line [2] =='Y':
            game_point = 1+3
        elif line[0] == 'A' and line [2] =='Z':
            game_point = 2+6
        elif line[0] == 'B' and line [2] =='X':
            game_point = 1+0
        elif line[0] == 'B' and line [2] =='Y':
            game_point = 2+3
        elif line[0] == 'B' and line [2] =='Z':
            game_point = 3+6
        elif line[0] == 'C' and line [2] =='X':
            game_point = 2+0
        elif line[0] == 'C' and line [2] =='Y':
            game_point = 3+3
        elif line[0] == 'C' and line [2] =='Z':
            game_point = 1+6
        total_points += game_point
        
print (total_points)

# w = 6     x = 0
# l = 0     y = 3
# d = 3     z = 6
# r = 1
# p = 2
# s = 3