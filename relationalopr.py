# comparison operator - used to compare values and returns a boolean result
a=5
b=6
print((a+1)==b)
print(a!=b)
print(a>(-b))
print((-a)<b)
print(a>=(-b))
print((-b)<=a)
print("\n")

# logical operator
x=3
y='Hi'
if x and y:
    print("True")
if x or y:
    print("True")
if not(not x):
    print("True")
print("\n")

# bitwise operator
n=7
if(n%2==0):
    print('True')
if(n&1==0):
    print('True')
else:
    print('False')
print(bin(n))
p=bin(n)
q=bin(1)
z=0b100^0b0001
print(z)