a=input("Enter your string: ")
print("\n")
print("1. for counting the alphabets\n2. for extracting the string\n3. for checking whether the given string is alphanumeric or not\n4. To end")
print("\n")
while(1):
    ch=int(input("Enter your choice: "))
    if ch==1:
        c=0
        for i in a:
            if i.isalpha():
                c+=1
        print(c)


    elif ch==2:
        word=input("Choose your extraction word: ")
        if word in a:
            print(word)
        else:
            print("Given word is not present in string")

        '''p=int(input('Starting Point: '))
        q=int(input('Ending Point: '))'''
       # print(a[11:17]) 

    elif ch==3:
        if a.isalnum():
            print("It is alphanumeric")
        else:
            print("It is not alphanumeric")

    elif ch==4:
        print("Program ended")
        break

    else:
        print("Invalid choice")