s = input("Enter score:")
score = float(s)
if (score < 0):
    print("error")
    quit()
elif (score > 1):
    print("error")
    quit()
else:
    if (score >= 0.9):
        print("A")
    elif (score >= 0.8):
        print("B")
    elif (score >= 0.7):
        print("C")
    elif (score >= 0.6):
        print("D")
    else:
        print("F")
