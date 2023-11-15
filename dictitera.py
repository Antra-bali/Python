
# Dictionary is a non-primitive datatype
a = {'key1': 1, 'key2': 2, 'key3': 3}
print("\n")
for i in a:
     print(i)
print(list(a))
print(type(list(a)))
print('Dictionary Iteration')
print('1.Through Dictionary keys()')
print('2.Through Dictionary values()')
print('3.Through Dictionary items()')
print('4.Exit')
print("\n")
while(1):
   
    ch=int(input('Enter Your Choice: '))
    if ch==1:
        for k in a.keys():
            print(k)
        print(a.keys())
        print(type(a.keys()))
        print(list(a.keys()))
        print(type(list(a.keys())))
        print("\n")
    elif ch==2:
         for j in a.values():
             print(j)
         print(a.values())
         print(type(a.values()))
         print("\n")
    elif ch==3:
         for i, j in a.items():
            print('Keys=',i, 'Values=',j)
         print(a.items())
         print(type(a.items()))
         print("\n")
    elif ch==4:
        break
    else:
        print("Invalid choice")

