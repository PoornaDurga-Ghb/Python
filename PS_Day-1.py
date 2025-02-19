# Positive and Negative numbers
num=int(input("enter a number"))
if num == 0:
    print("0 is neither positive nor negative")
elif num > 0:
    print("positive number")
else:
    print("Negative number")

# Even or Odd
num=int(input("enter a number"))
if num == 0:
    print("0 is neither Even nor Odd")
elif num % 2 == 0:
    print("even number")
else:
    print("odd number")

# Eligibility to vote
age=int(input("enter age"))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")

# greatest of 2 numbers
num1=int(input("enter a 1st number"))
num2=int(input("enter a 2nd number"))
if num1 == num2:
    print("both are equal")
elif num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")

# pass and fail
num1=40
if num1 >= 40:
    print("pass")
else:
    print("fail")

# using ternary operator
marks = 20
marks = "pass" if marks >= 40 else "fail"
print(marks)

# day of week
days = 6
if days == 1:
    print("monday")
elif days == 2:
    print("tuesday")
elif days == 3:
    print("wednesday")
elif days == 4:
    print("thursday")
elif days == 5:
    print("friday")
elif days == 6:
    print("saturday")
elif days == 7:
    print("sunday")
else:
    print("there are only 7 days in a week")

# calculator
operation = input("enter operation which you want to perform from 'add or sub or mul or div'").lower()  #to convert all uppercase to lower case strings
a=10
b=20
if operation == 'add':
    print(a + b)
if operation == 'sub':
    print(a - b)
if operation == 'mul':
    print(a * b)
if operation == 'div':
    if b == 0:
        print("division is not possible")
    else:
        print(a / b)

# name of month based on month number
month_name = 10
if month_name == 1:
    print("January")
elif month_name == 2:
    print("February")
elif month_name == 3:
    print("March")
elif month_name == 4:
    print("April")
elif month_name == 5:
    print("May")
elif month_name == 6:
    print("June")
elif month_name == 7:
    print("July")
elif month_name == 8:
    print("August")
elif month_name == 9:
    print("September")
elif month_name == 10:
    print("October")
elif month_name == 11:
    print("November")
elif month_name == 12:
    print("December")
else:
    print("There are only 12 months in a year")

# Greatest of 3 numbers
n1 = 10
n2 = 20
n3 = 9
greatest = n1 if n1 > n2 and n1 > n3  else (n2 if n2 > n1 and n2 > n3 else n3)
print("Greatest Number" , greatest)

# leap year or not
year = int(input(" enter a year"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year," is leap year")
else:
    print(year,"not a  leap year")

# character entered is vowel,consonant or neither
char = input("enter any single character").lower()
if len(char) != 1:
    print("invalid input")
elif char in ['a','e','i','o','u']:
    print("vowel")
elif char.isalpha():
    print("consonants")
else:
    print("special characters or symbols not accepted")

# grade of student based on marks
marks = int(input("enter marks"))
if marks > 100:
    print("invalid input")
elif marks == 90 and marks <= 100:
    print("Grade A")
elif marks == 80 and marks <=89:
    print("Grade B")
elif marks == 70 and marks <=79:
    print("Grade C")
else:
    print("Fail")

# checking if 3 sides lenth forms a triangle
len1,len2,len3 = 10, 45, 30
if len1 + len2 < len3 or len1 + len3 < len2 or len2 + len3 < len1:
    print("yes, it forms a triangle")
else:
    print("No, as we cannot form a traingle with given lengths")
