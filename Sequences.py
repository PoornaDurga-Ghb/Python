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