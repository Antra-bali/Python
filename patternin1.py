"""
*
**
***
****
*****
print using 1 print statement"""
'''r=int(input())
for i in range(r+1):
    print('* '*i)'''
"""
     *
    **
   ***
  ****
 *****   
"""
'''for i in range(6,-1,-1):
    print('*'*i)
print("\n")'''
j=0
for i in range(6,0,-1):
    j+=1
    print("  "*i,'* '*j)


r=5
for i in range(1,r+1):
    print("  "*(r-i),i*"* ")


'''print("\n")
r=5
for i in range(1,r+1):
    print(" "*(r-i),i*"* ")
print("\n")
for i in range(r,-1,-1):
    print(" "*(r-i),i*"* ")
print("\n")
r=5
for i in range(1,r+1):
    if i!=r:
        print(" "*(r-i),i*"* ")
for i in reversed(range(1,r+1)):
    
        print(" "*(r-i),i*"* ")
#print("\n"*5)
r=5
for i in range(1,r+1):
    if i!=r:
        print(" "*(r-i),i*"* ")
for i in reversed(range(1,r+1)):
    if i==2:
        print(" ")
    else:
        print(" "*(r-i),i*"* ")'''
'''r=7
for i in range(1,r+1):
    if i!=r:
        if i==4:
            print(" ")
        else:
            print(" "*(r-i),i*"* ")
for i in reversed(range(1,r+1)):
    if i==4:
        print(" ")
    else:
        print(" "*(r-i),i*"* ")'''