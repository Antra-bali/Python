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