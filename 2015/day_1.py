file = open("2015/input.txt", "r")
floor_no = 0
count = 0
index=[]
for line in file:
    for i in line:
        if i == '(':
            floor_no +=1
            count +=1
        if i == ')':
            floor_no -=1
            count +=1
        if floor_no == -1:
            index.append(count)
print("Part 1 : ",floor_no)
print("Part 2 : ",index)