fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
for line in fhandle:
    sline = line.rstrip()
    temp = sline.split()
    i = 0
    for word in temp:
        i = i + 1
        if 'From' in word:
            if 'From:' not in word:
                count = count + 1
                print(temp[i])
print("There were", count, "lines in the file with From as the first word")
