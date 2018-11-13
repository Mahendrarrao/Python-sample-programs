fname = input("enter filename")
fhandle = open(fname)
exist = []
for line in fhandle:
    sline = line.rstrip()
    temp = sline.split()
    for word in temp:
        if word in exist:
            continue
        exist.append(word)
        exist.sort()
print(exist)
