

# try to define variables using some meaningful context and follow pascal and snakes rules
# naming conventions-3 types
# pascal case = identifying distinct/different words in one word using capital letters of each first word.(HumanBeing)
RandomInput = int(input())
print(RandomInput)
# ,snake case = all small letters seperated by an underscore(_) to differentiate words.(human_being)
random_input = int(input())
print(random_input)
# , camel case = first word is small letter and next words will start with caps(not used in python).(humanBeing)
# we use all caps for defining a constant
# Truthy values and falsy values
# truthy = all numbers except 0,true and all strings except empty strings
# falsy = 0,false,''
 
# conversions

# 1111101 - 1*1 + 0*2 + 1*4 + 1*8 + 1*16 + 1*32 + 1*64
# 125
# 1256 = 6 40 64 512 = 622
# hexadecimal
# 10-A .....15-F
# AF1= 1+240+2560 = 2801
# 111-binary=7
# 111-octal=1+8+64=73
# 111-hex=1+16+256=273


num=20
num += 2
print(num)
num /= 2
print(num)
num //= 2
print(num)
num **= 2
print(num)

print(None and 2)
print(10 and 'str')
print('' and 'str')
print(56 and '')
print("-------------")
print(None or 2)
print(10 or 'str')
print('' or 'str')
print(56 or '')
print(True or False)
print("-------------")
print(100 | 1111)
print(10 | 11)
print(1 | 1)
print(599 | 999)
print(10 | 11)
print(1 | 1)
print(599 | 999)
print(bin(2))
print(12 ^ 14)

# SHIFT
print("shift")
print(15 << 1)
print(15 >> 1)
print(14 << 1)
print(14 >> 1)


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

        # ------OR---------

for i in range(0,21,2):
    print(i)



hello=int(input("enter any no."))
while hello == 10:
    print("nums = ",hello)
    hello += 2

i=5
while i < 26:
    if i%2 == 0:
        print("even",i)
    else:
        print("odd",i)
    i+=1

start=1
while start < 11:
    roll=1
    if start!=5 and start!=7:
        while roll < 31:
            print(start,roll)
            roll += 1
    start += 1