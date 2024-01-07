#1. 


n = int(input("Введите число N: "))
i = 1
while i**2 <= n:
    print(i**2, end=" ")
    i += 1


#2.

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

i = a
while i <= b:
    print(i**3, end=" ")
    i += 1


#3.


x = float(input("Введите число: "))
n = int(input("Введите степень: "))

result = 1
for i in range(n):
    result *= x

print(x, "в степени", n, "=", result)


#4.

n = int(input("Введите число: "))

result = 1
for i in range(1, n+1):
    result *= i

print(n, "! =", result)


#5.


n = int(input("Введите количество чисел Фибоначчи: "))

a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c


#6.


n = int(input("Введите число: "))

digits = []
while n > 0:
    digit = n % 10
    digits.append(digit)
    n //= 10

digits.reverse()
print("Цифры числа:", end=" ")
for digit in digits:
    print(digit, end=" ")


#7.


n = int(input("Введите число: "))

sum_even = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_even += digit
    n //= 10

print("Сумма четных цифр:", sum_even)


#8.

n = int(input("Введите число: "))

sum_digits = 0
prod_digits = 1
while n > 0:
    digit = n % 10
    sum_digits += digit
    prod_digits *= digit
    n //= 10

print("Сумма цифр:", sum_digits)
print("Произведение цифр:", prod_digits)
