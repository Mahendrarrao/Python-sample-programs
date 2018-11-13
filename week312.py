def convert(text):
    mod1 = text.find(':')
    lstring = text[mod1+1:]
    string = lstring.lstrip()
    val = float(string)
    return val

fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
total = 0
avg = 0
avg = float(avg)
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    val = convert(line)
    count = count + 1
    total = total + val
avg = total/count
print("Average spam confidence:",avg)
