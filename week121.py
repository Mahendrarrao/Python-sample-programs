import re
filename = input("enter filename")
fhandle = open(filename)
numberlist = list()
sum = 0
for line in fhandle:
    flist = re.findall('[0-9]+',line)
    for item in flist:
        if(len(item) > 0):
            numberlist.append(item)
print(numberlist)
for number in numberlist:
    number = float(number)
    sum = sum + number
print(sum)
