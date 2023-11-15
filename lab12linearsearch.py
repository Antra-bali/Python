a=[1,2,3,4,5,12,6,14]
x=int(input("Enter the element you want to search: "))

for i in range(len(a)):
    if a[i]==x:
        print('Element',a[i],'found at Index',i,)
        break
else:
    print('Element not found')

    ''' OR
   use  flag'''