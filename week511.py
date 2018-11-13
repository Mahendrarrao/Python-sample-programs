fname = input("Enter file name: ")
fhandle = open(fname)
list = []
counts = dict()
for line in fhandle:
    sline = line.rstrip()
    temp = sline.split()
    i = 0
    for word in temp:
        i = i + 1
        if 'From' in word:
            if 'From:' not in word:
                list.append(temp[i])
for word in list:
    counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword,bigcount)
