'''for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print("W ",end="")
        else:
            print("B ",end="")
    print()
# ord - ASCII value
print(ord("A"))'''
a=input()
#if(ord(a[0:1]))
i=ord(a[0])- ord('a')
print(i)
j=8-int(a[1])
print(j)
if(i+j)%2==0:
    print("w")
else:
    print("b")


