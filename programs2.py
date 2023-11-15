'''#1
a=int(input())
b=int(input())
print(a-(-b))

      #or
sum=a
for i in range(b):
    sum=sum+1
print(sum)

     #or

while(b!=0):
    carry= a&b
    a=a^b
    b=carry<<1
print(a)


#2
c=int(input())
for i in range(c+1):
    for j in range(i):
        print("*",end=" ")
    print()
      
#3
d=int(input())
e=int(input())
ch=input()
if ch=='+':
    print(d+e)


#4
chh=input("Convert to F/C")
if chh=='C':
    num=float(input("Enter temp in F"))
    c=(5/9)*(num-32)
    print(c,chr(176))
elif chh=='F':
    num=float(input("Enter temp in C"))
    f=(9/5)*num+32
    print(f)'''
'''
#5
a=int(input())
b=int(input())
mul=0
for i in range(b):
    mul=mul+a
print(mul)

#6
c=int(input())
for i in range(c+1):
    for j in range(c-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

for i in range(1, c + 1):
    # Print spaces before the stars
    for j in range(c - i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(i):
        print("*", end=" ")
    
    # Move to the next line for the next row
    print()
#7
a=int(input())
ch=int(input("1.Square Root\n2.Power\n3.Factorial\n"))
if ch==1:
    print(a**0.5)
elif ch==2:
    n=int(input("Enter power"))
    print(a**n)
elif ch==3:
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)
'''


'''#8		
a=input()
b=[]
for i in a:
    if i not in b:
        print(i,end="")
        b.append(i)'''
    
    
'''    
print(bool(False))
print(None)
a=None
print(a)'''
def A(a):
    b=""
    for i in a:
        if i not in b:
            b+=i
    return b
a=input()
print(A(a))