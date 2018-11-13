fname = input("Enter file name: ")
fhandle = open(fname)
list = []
counts = dict()
for line in fhandle:
    sline = line.rstrip()
    temp = sline.split()
    for word in temp:
        if 'From' in word:
            if 'From:' not in word:
                time_temp = temp[5].split(":")
                list.append(time_temp[0])
for word in list:
    counts[word] = counts.get(word,0) + 1
final = []
for key, value in counts.items():
    final.append( (key,value) )
result = sorted(final)
for hour,occur in result:
    print(hour,occur)
