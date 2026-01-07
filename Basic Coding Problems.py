1)interchanging digit

number = 123
total = 0

while number > 0:
    digit = number % 10 
    total += digit      
    number = number // 10 

print(f"Sum of digits is: {total}")

2)Reversing a number 

number = 456
reversed_num = 0

while num > 0:
    last_digit = num % 10
    reversed_num = (reversed_num * 10) + last_digit
    num = num // 10

print(f"Reversed number: {reversed_num}")

3)Creating Table

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end=" ") 
    print()

4) number = [0.8, 0.4, 0.9, 0.2, 0.6]
smallest = number[0]

for e in number:
    if e < smallest:
        smallest = e

print(f"Lowest number: {smallest}")

5) Fibonancci sequence

a, b = 0, 1
print("Fibonacci:", end=" ")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

6) Checking Prime number

num = 17
_prime = True

for i in range(2, num):
    if num % i == 0:
        _prime = False
        break

print(f"Is {num} prime? {_prime}")

7) #Are u adult or not

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an Adult.")
elif age >= 13:
    print("Faaaah! Not an adult.")
else:
    print("error.")

8)Grading 

score = 85

if score >= 90:
    grade = "A (Nerd)"
elif score >= 75:
    grade = "B (Perfect)"
elif score >= 50:
    grade = "C (Koi baat ni)"
else:
    grade = "F (Faaaah!)"

print(f"Your grade: {grade}")

9) Calculator

print("Simple Python Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error 404")
else:
    print("Typo by you.")
