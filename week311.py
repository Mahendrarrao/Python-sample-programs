fname = input("enter filename")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    upper_case = line.upper()
    print(upper_case)
