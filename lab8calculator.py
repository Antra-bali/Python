a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
d=0
print("Operations:- \n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Remainder\n5 for Division\n6 for Power\n7 for Squareroot\n8 for Binary Conversion\n9 for Octal Conversion\n10 for Hexadecimal Conversion ")
while(d!=11):
    c=str(input("Enter your choice: "))
    d=int(c)
    if(d==1):
        sum=a+b
        print(a,"+",b,"=",sum)
    elif(d==2):
        sub=a-b
        print(a,"-",b,"=",sub)
    elif(d==3):
        mul=a*b
        print(a,"x",b,"=",mul)
    elif(d==4):
        rem=a%b
        print(a,"%",b,"=",rem)
    elif(d==5):
        if(b==0):
            print("Division not valid")
        else:
            div=a/b
            print(a,"/",b,"=",div)
    elif(d==6):
        pow=a**b
        print(a,"^",b,"=",pow)
    elif(d==7):
        s1=a**0.5
        print("Sqrt of",a,"=",s1)
        s2=b**0.5
        print("Sqrt of",b,"=",s2)
    elif(d==8):
        print("Binary of ",int(a),"=",bin(int(a)))
        print("Binary of ",int(b),"=",bin(int(b)))
    elif(d==9):
        print("Octal of ",int(a),"=",oct(int(a)))
        print("Octal of ",int(b),"=",oct(int(b)))
    elif(d==10):
        print("Hexadecimal of ",int(a),"=",hex(int(a)))
        print("Hexadecimal of ",int(b),"=",hex(int(b)))
    elif(d==11):
        break
    else:
        print("Invalid Operation")
