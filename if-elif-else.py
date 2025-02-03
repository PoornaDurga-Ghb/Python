#if - elif - else
num1 = 3.24567890
if num1 > 0 and num1 != 1:
    print("+ve")
elif num1 == 1:
    print("one")
elif num1 == 0:
    print("zero")
elif num1 == -1:
    print("-1")
elif num1 == -2:
    print("-2")
else:
    print("-ve")


 
current_bill_units = int(input("enter units"))
if current_bill_units <= 100:
    if current_bill_units <= 50:
        print("current bill amount = 0")
    else:
        print("current bill amount = ",current_bill_units * 50)
else:
    if current_bill_units <= 200:
        print("current bill amount = ",current_bill_units * 100)
    else:
        if current_bill_units <= 300:
            print("current bill amount = ",current_bill_units * 150)

for i in range(0,21):
    if i%2 == 0:
        print("even num = ",i)
    else:
        print("odd number = ",i)
