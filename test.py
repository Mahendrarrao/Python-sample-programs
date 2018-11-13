fname = input("enter filename")
fhandle = open(fname)
for line in fhandle:
  if 'apan' in line:
      print(line)
