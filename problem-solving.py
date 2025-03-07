# sum of odd digits of a given number
num = 56473829
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    if digit % 2 != 0:
        sum += digit
    temp //= 10
print("sum of odd digits = ",sum)

# Armstrong number - a number which is equal to sum of its own digits each raised to a power of number of digits
num = 153
def armstrong_number(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10 
        sum += digit ** len(str(num))
        temp //= 10
    return sum == num
if armstrong_number(num):
    print("armstrong num")
else:
    print("not an armstrong num")
# Armstrong numbers in given range
num1, num2, sum = 150, 9474, 0
for i in range(num1 , num2+1):
    if armstrong_number(i):
        print(i)

# prime number function
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
# print(is_prime(0))


# finding smallest prime digit in a given number
num = 35452
temp = num
smallest_prime = []
while temp > 0:
    digit = temp % 10
    if is_prime(digit):
        smallest_prime.append(digit)
    temp //= 10
if smallest_prime:
    print(min(smallest_prime) , " is the smallest prime number")
else:
    print("There are no prime numbers in ", num)

