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