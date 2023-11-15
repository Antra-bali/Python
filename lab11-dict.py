a="Welcome to Python World"
print("\n")
print('Original string:',a)
print('1.Count no of alphabets')
print('2.Extract Character using range')
print('3.String is alphanumeric or not')
print('4.Exit')
print("\n")
while(1):
    
    ch=int(input('Enter your choice: ')) 
    if ch==1:
     l=len([ele for ele in a if ele.isalpha()])
     print(l)
     print("\n")
    elif ch==2:
     start=int(input('Enter start range: '))
     end=int(input('Enter end range: '))
     print(a[start:end])
     print("\n")
    elif ch==3:
         print(a)
         b=a.isalnum()
         print(b)
         print("\n")
    elif ch==4:
        break
    else:
       print('Invalid choice')