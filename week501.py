h = input("Enter Hours:")
hrs = float(h)
r = input("Enter rate:")
rate = float(r)
total_pay = 0.0
extra_hrs = 0.0
extra_pay = 0.0
if (hrs > 40):
    extra_hrs = hrs - 40
    extra_pay = extra_hrs*rate*1.5
    hrs = hrs - extra_hrs
total_pay = hrs*rate + extra_pay
print(total_pay)
