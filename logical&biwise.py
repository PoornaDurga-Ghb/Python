logical and bitwise operators
# LOGICAL OPs
# we use Boolean values instead of 0's and 1's in python instead of symbols
# ->in logical ops the operands depends on truthy and falsy values and returns operands
# ->for numbers it checks the first value and if its true then o/p depends on second value and similarly if first value is true then o/p returns the false value directly as output becomes false.
# ->BITWISE OP's - AND, OR, XOR, <<, >>
# they return some value by doing operations on bits(binary bits) unlike logical ops as they return only operands 
# ->XOR- if any 2 values (00 or 11) are equal then it returns false or 0 but if both values are different then o/p will be 1 or true in Bitwise XOR

# CONTROL STATEMENTS - controls flow of execution of a code - conditional, loops and jump statements  

num=20
num += 2
print(num)
num /= 2
print(num)
num //= 2
print(num)
num **= 2
print(num)
# logical
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
# bitwise
print(100 | 1111)
print(10 | 11)
print(1 | 1)
print(599 | 999)
print(10 | 11)
print(1 | 1)
print(599 | 999)
print(bin(2))
# XOR
print(12 ^ 14)

# SHIFT
print("shift")
print(15 << 1)
print(15 >> 1)
print(14 << 1)
print(14 >> 1)

# logical
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

# slicing using strings with positive indexing
str1="veerashankarreddy, mokke kadha ani pikesthe peeka kostha"
print(str1[7: ])
print(str1[7: 23])
print(str1[24])
print(str1[23: 7: -1])
print(str1[23: 7])

# slicing using strings with negative indexing
print(str1[-24: -7])
print(str1[-7:-24: -1])
print(str1[-4: -30: -3])

# to know the address value assigned in memory block for a particular variable
str1='hello'
print(id(str1))
str2='hello'
print(id(str2))
str3='hello'
print(id(str3))
str4='world'
print(id(str4))
str5='world'
print(id(str5))
str6='world'
print(id(str6))

# ..................few datatypes in python.......................
# int(example:2,56,12345, and so on)
2
print(type(2))
# float(example:21.23,5.6,12345.33333, and so on)
5.6
print(type(5.6))
# complex(example:2+3j,6+7j, and so on)
6+7j
print(type(6+7j))
# string(example:'hey',"there", and so on)
str1='hey'
print(type(str1))


# strings are immutable as their sub strings cannot be changed once declared but we can re-assign the entire string to avoid ambiguity in python
str2='Hey There!! How you doing..'
print(str2[12]) 
#now lets try to change a specific index value
str2[12]='p'
print(str2[12])  #it throws an error as strings are immutable and connot be changed but can be re-assigned (the entire string should be changed).

# an alternative is re-assigning it.
str2='Hey There!! pow you doing..'
print(str[12])
