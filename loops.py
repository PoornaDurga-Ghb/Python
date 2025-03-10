# Multiplication table
def multiplication_table(num):
    for i in range(1,21):
        print(num, 'x', i, '=', num * i )

print(multiplication_table(5))

# Factorial of a number using while loop
def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(Factorial(4))

# Printing all numbers from 1 to 100 that are divisible by 3 and 5
def divisibility_check():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
        
divisibility_check()