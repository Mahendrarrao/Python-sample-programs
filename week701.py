largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        val = float(num)
        if (val < 0):
            print("Inavlid input")
            continue
    except:
        print("Inavlid input")
        continue
    if (val > largest):
        largest = val
    if (smallest is None):
        smallest = val
    elif (val < smallest):
        smallest = val
print(int(largest))
print(int(smallest))
