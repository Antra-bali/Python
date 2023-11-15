
# To convert temperature from celsius to farenheit
#c=int(input('Enter the temperature in Celsius: '))
def c_to_f():
    f=(c*9/5)+32
    print(c,"°C is equal to",f,"°F")  # option+shift+8
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
        c_to_f()
        
    elif ch==2:
        far=int(input('Enter the temperature in Farenheit: '))
        f_to_c()
    elif ch==3:
        break
    else:
        print("Invalid choice")