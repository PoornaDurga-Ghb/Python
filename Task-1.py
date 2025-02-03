# The comments are represented by hashtag(#) and these are ignored by the computer

#operations using numbers
print(120+120)
print(120-120)
print(120*120)
print(120/120)
print(120//120)
print(120**120)

#operations using variables
me=84
you=49
print(me+you)
print(me-you)
print(me*you)
print(me/you)
print(me//you)
print(me**you)

#using strings
print("Magadheera")
print('Bahubali')
print("Bahubali-2")

#using len
print(len("Magadheera"))
hello="world"
print(len(hello))
hello="earth"
print(len(hello))

# using type operator
poorna="999.999"
print(type(poorna))

# using index 
index_var="okkokadini kaadhu sherkhan..........vandha mandhini okesari rammanu"
print(index_var[5])
print(index_var[18])

# using index with range (slicing)
print(index_var[10:30])
a=2+10j
b=3+9j
print(a+b)
print(a-b)
print(a/b)
print(a**b)
print(int(True))
print(23 <= 23)
# ------------------day-2------------------------------
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

#complex numbers and operations
a=5+9j
b=3+8j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# print(a//b)  #throws an error as complex numbers doesn't support integer division
print(a**b)
# print(a%b)   #modulo divison is also not supported for complex numbers

#Typecasting
print(int(True))
print(float(False))
print(complex(True))
print(bool(True))
print(str(True))

#list and indexing
hello=[1,7,0,'sleep',"cry", [9,'hhh',['hell',2,3678]]]
print(hello)
print(len(hello))
print(hello[5])
print(hello[3])
print(hello[2: ])
print(hello[-5: -1])
print(hello[-4: ])
#lists are mutable so we can change their values using indexing
hello[5][2][0]="heaven"
print(hello)
hello[5][2][2]=891011
print(hello)
hello[1]=21
print(hello)
print(hello[1]==22)
print(hello[1]==21)
print(hello[5][2][1]==2)
print(type(hello))
print(len(hello[5][2][0]))

#tuple and indexing on tuples
world=(52,4,'ehehehe',True)
print(world[2])
print(world[0: ])
print(world[-1])
print(world[-1: -3: -2])
print(len(world))
#tuples are immutable so we cannot change their values once declared
#example :the below example throws a  "tuple object doesnot support item assignment"
# world[2]='hahaha'
# print(world)

#range
print(list(range(1,100)))
print(list(range(100,1,-1)))
print(tuple(range(1,100)))
print(tuple(range(1,100,3)))
print(tuple(range(100,1,-3)))
print(bool(range(1,100)))
print(bool(range(100,1)))

#range-prints the values within the given range
list1=['abbraka','dabra','dabraka','abbra',5252,True]
for i in range(0,len(list1)):
    print(i,list1[i])


#dictionary--key value pairs
# keys must be unique and value must not be unique, and keys can be strings or numbers
# we can access value using keys but we can't use values to access keys and we can change values using indexing as dictionaryis mutable
# if duplicate keys are given then it updates to last given duplicate key and we can also delete a key
dict1={1:'hello',2:'there',3:'nice',4:'meet',5:'you'}
print(dict1[2])
print(dict1[1])
print(dict1[2])
print(dict1[5])
dict1['6']='!!!!!'
dict1['6']='****'
dict1[6]='hhhhhh'
print(dict1)
print(len(dict1))


#set datatype-colllection of unique,unordered,finite elements and set is not indexable and defined with {}
set1={2,4,2,2,2,4,5,5,6,2}
print(set1)
set2={'hello','hello again',12,12,'hello','hello again','ok bye'}
print(set2)
print(len(set1))

# none datatype- for memory efficiency and used to store nothing in memory block when we dont want anything inside that memory block
num1=57
num1=None
print(num1)
print(type(num1))

# c=int(input("enter a value"))
# print(c)
a=int(input("enter 1st value"))
b=int(input("enter 2nd value"))
print("Result=",a+b)
print("Result=",a-b)
print("Result=",a*b)
print("Result=",a/b)
print("Result=",a//b)
print("Result=",a**b)
print("Result=",a%b)