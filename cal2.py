a=int(input("Enter the first number: "))
d=0
ans=a
print("Operations:- \n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Remainder\n5 for Division\n6 for Power\n7 for Squareroot\n8 for Binary Conversion\n9 for Octal Conversion\n10 for Hexadecimal Conversion ")
while(d!=11):
    c=str(input("Enter your choice: "))
    d=int(c)
    if(d==1):
        b=int(input("Enter the second number: "))
        a=ans
        ans=a+b
        print(a,"+",b,"=",ans)
    elif(d==2):
        b=int(input("Enter the second number: "))
        a=ans
        ans=a-b
        print(a,"-",b,"=",ans)
    elif(d==3):
        b=int(input("Enter the second number: "))
        a=ans
        ans=a*b
        print(a,"x",b,"=",ans)
    elif(d==4):
        b=int(input("Enter the second number: "))
        a=ans
        ans=a%b
        print(a,"%",b,"=",ans)
    elif(d==5):
        b=int(input("Enter the second number: "))
        a=ans
        if(b==0):
            print("Division not valid")
        else:
            ans=a/b
            print(a,"/",b,"=",ans)
    elif(d==6):
        b=int(input("Enter the second number: "))
        a=ans
        ans=a**b
        print(a,"^",b,"=",ans)
    elif(d==7):
        a=ans
        ans=a**0.5
        print("Sqrt of",a,"=",ans)
    elif(d==8):
        print("Binary of ",int(ans),"=",bin(int(ans)))
    elif(d==9):
        print("Octal of ",int(ans),"=",oct(int(ans)))
    elif(d==10):
        print("Hexadecimal of ",int(ans),"=",hex(int(ans)))
    elif(d==11):
        break
    else:
        print("Invalid Operation")
print("Final value",ans)
