a=[10,10.5,'Apple',34,47]
print("\n")
len=len(a)
'''
print("\n")
print(*a)
# use * to remove the list brackets
len=len(a)
# 1. Using for loop with range
#for i in range(len):
#    print(a[i])
# 2. Using for loop
for i in a:
    print(i)
print("\n")
i=0
# Using while loop
while i in range(len):
    print(a[i])
    i+=1
print("\n")

[print(i) for i in a]     # [] syntax
(print(i) for i in a)     # no output
4. Using comprehension
a=[]
[print(i,end=" ") for i in range(10000000)] # comprehension - easy(compact) syntax 

# 5. Using enumeration
for i, val in enumerate(a):    # have to create a variable for the values and i is for the index
    print(i,"-",val)
b=[[10,20],[30,40],[50,60]]
for i,val in b:
    print(i,"-",val)
for i,val in enumerate(b):
    print(i,"-",val)
for i,m,n in enumerate(b):
    print(i,"-",m,"-",n)
"""
does not work with range
for i,val in range(len):
    print(i,",",val)"""

'''
print("List Iteration")
print("1. Using for loop (Variable)")
print("2. Using for loop (range)")
print("3. Using while loop")
print("4. Using List Comprehension")
print("5. Using Enumeration")
print("6. Exit")
print("\n")
while(1):

    ch=int(input("Enter your choice: "))
    if ch==1:
        for i in a:
            print(i)
        print("\n")
    elif ch==2:
        for i in range(len):
            print(a[i])
        print("\n")
    elif ch==3:
        i=0
        while i in range(len):
            print(a[i])
            i+=1
        print("\n")
    elif ch==4:
        [print(i) for i in a]
        print("\n")
    elif ch==5:
        for i, val in enumerate(a):   
            print(i,"-",val)
        print("\n")
    elif ch==6:
        break
    else:
        print('Invalid choice')
        