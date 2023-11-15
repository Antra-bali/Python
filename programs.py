# 1 without + operator
def add_without_operator(num1, num2):
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1

    return num1

# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = add_without_operator(num1, num2)
print("Sum of the two numbers without using addition operator:", result)


# 2 right angled triangle
# Input
num_rows = int(input("Enter the number of rows: "))

# Print the right-angled triangle
for i in range(1, num_rows + 1):
    # Print spaces before the stars
    for j in range(num_rows - i):
        print(" ", end="")
    
    # Print stars
    for k in range(i):
        print("*", end="")
    
    # Move to the next line for the next row
    print()


# 3 calculator
# mini calculator using functionc +,-,*,/,%
# function for addition
def add(a,b):
    return a+b
# function for subtraction
def sub(a,b):
    return a-b
# function for multiplication
def mul(a,b):
    return a*b
# function for division
def div(a,b):
    return a//b
# function for remainder
def rem(a,b):
    if b==0:
        return "cannot"
    return a%b

# main
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Exit")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
while(1):
    c=int(input("Enter your choice: "))
    if c==1:
        print(add(a,b))
    elif c==2:
        print(sub(a,b))
    elif c==3:
        print(mul(a,b))
    elif c==4:
        print(div(a,b))
    elif c==5:
        print(rem(a,b))
    elif c==6:
        break
    else:
        print("Invalid Choice")

# 4 temp

# To convert temperature from celsius to farenheit
#c=int(input('Enter the temperature in Celsius: '))
def c_to_f():
    f=(c*9/5)+32
    return c,"°C is equal to",f,"°F"  # option+shift+8
    print("\n")

# To convert temperature from farenheit to celsius
def f_to_c():
    cal=(far-32)*5/9
    print(far,"°F is equal to",cal,"°C")
    print("\n")
print("1. To convert temperature from Celsius to Farenheit\n2. To convert temperature from Farenheit to Celsius\n3. To exit from the program")
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        c=int(input('Enter the temperature in Celsius: '))
        print(c_to_f())
        
    elif ch==2:
        far=int(input('Enter the temperature in Farenheit: '))
        f_to_c()
    elif ch==3:
        break
    else:
        print("Invalid choice")

# 5 without *

def multiply_without_operator(num1, num2):
    result = 0
    for _ in range(abs(int(num2))):
        result += num1 if num2 > 0 else -num1

    return result

# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the product without using the multiplication operator
result = multiply_without_operator(num1, num2)

# Output
print(f"Multiplication of {num1} and {num2} without using the multiplication operator is: {result}")

# 6
def print_left_angle_triangle(rows):
    for i in range(1, rows + 1):
        # Print stars
        for j in range(i):
            print("*", end="")
        # Print spaces
        for k in range(rows - i):
            print(" ", end="")
        # Move to the next line for the next row
        print()

# Input
rows = int(input("Enter the number of rows: "))

# Print the left-angled triangle
print_left_angle_triangle(rows)

# 7 
import math

# Function to calculate the square root
def calculate_square_root(num):
    return math.sqrt(num)

# Function to calculate the power
def calculate_power(base, exponent):
    return base ** exponent

# Function to calculate the factorial
def calculate_factorial(num):
    if num == 0:
        return 1
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Input
num1 = float(input("Enter a number: "))
choice = int(input("Choose an operation:\n1. Square Root\n2. Power\n3. Factorial\nEnter your choice (1, 2, or 3): "))

# Perform the selected operation
if choice == 1:
    result = calculate_square_root(num1)
    print(f"Square Root of {num1} is: {result}")
elif choice == 2:
    exponent = int(input("Enter the exponent: "))
    result = calculate_power(num1, exponent)
    print(f"{num1} raised to the power of {exponent} is: {result}")
elif choice == 3:
    if num1 < 0 or not num1.is_integer():
        print("Factorial is defined for non-negative integers only.")
    else:
        result = calculate_factorial(int(num1))
        print(f"Factorial of {int(num1)} is: {result}")
else:
    print("Invalid choice. Please choose 1, 2, or 3 for the operation.")

# 8  
def remove_duplicates_and_print_unique(input_string):
    unique_elements = []
    for char in input_string:
        if char not in unique_elements:
            unique_elements.append(char)
    unique_string = ''.join(unique_elements)
    return unique_string

# Input
given_string = input("Enter a string: ")

# Call the function to remove duplicates and print unique elements
result = remove_duplicates_and_print_unique(given_string)

# Output
print("Unique elements in the given string:", result)



print(' "hi"')
a='a'
b='b'
c='z'
print(a<b<c)
d='0123456789'
print(d[0:8:4])
print(2 and 3)
print(2 or 1)
print(2 and 1 or 3)
x=5
y=6
print(bin(5))
print(bin(3))
print(x>8 and y>9)
print(x ^ y)
print(x>4 and y>6)
print(x>6 and y>5)
print(x>4 or y>6)
print(x>6 or y>5)
print(x>4 or y>5)
print(x>6 or y>7)

t=(1,5,2,3,9,0,'a','b')
tt=t+(12,'c')
c=t[2:6]
print(t)
print(tt)
print(c)
p=(45,67,23)
print(tt+p)

s={1,2,3,9}
print(s)
s2=set([3,4,5,9])
print(s2)
#s.add(0)
#print(s)
#s.remove(2)
print("\n")
#print(s)
print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))

d={1:5,2:10,3:15,5:25,4:20,7:35}
print(d.keys())
print(d.values())
print(d.items())

print(sorted(d.items()))
print(sorted(d.values()))
print(sorted(d.keys()))
a=sorted(d.keys(),reverse=True)
print(a)