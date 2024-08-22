


file = open("test.txt", "r")
main_dict = {}
for line in file:
    line = line.strip()
    res = line.split(":")
    # a = 
    main_dict.update({res[0]:res[1].strip()})
    # exec("%s = %d" % (res[0],res[1]))
print(main_dict)

while not int(main_dict["root"]):
    print("p")
