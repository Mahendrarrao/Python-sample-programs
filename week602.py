def computepay(hours,rate):
    total_pay = 0.0
    extra_hrs = 0.0
    extra_pay = 0.0
    if (hours > 40):
        extra_hrs = hours - 40
        extra_pay = extra_hrs*rate*1.5
        hours = hours - extra_hrs
    total_pay = hours*rate + extra_pay
    return total_pay

h = input("Enter Hours:")
hrs = float(h)
r = input("Enter rate:")
rte = float(r)
p = computepay(hrs,rte)
print("Pay",p)
