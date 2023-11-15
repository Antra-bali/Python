'''a=20//3
print(a)
b=20/3
print(b)'''

x=[1,2,3,4,5,6,7,8,9,10]
target=19
a=0
b=len(x)-1
while(a<b):
    mid=(a+b)//2
    if x[mid]==target:
        print("Element found")
        break
    elif x[mid]>target:
        b=mid
    elif x[mid]<target:
        a=mid+1

else:
    print("Element not found")

