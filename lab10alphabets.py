'''a='Welcome to Python world'
count=0
for i in a:
    count+=1
print(count)
count1=0
for i in a:
    if i.isalpha():
        count1+=1
print(count1)
  '''  
a=input("Enter: ")
#if a.isalnum():
#    print("It is alphanumeric")
#else:
#    print("It is not alphanumeric")


p=int(input('Starting Point: '))
q=int(input('Ending Point: '))
print(a[p:q])      # string slicing
'''for i in range(p,q+1):
    if a[i].isalpha():
        print(a[i],end="")

    or 
'''
print("\n")
b="hi im mahi"
print(b[3:5])

