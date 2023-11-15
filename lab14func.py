def fname(a,b,c):
    print("Hii")
    d=a+b+c
    print(d)
print("Bye")
'''a=10
b=20 
c=30
a=int(input())
b=int(input())
c=int(input())
fname(a,b,c)
fname(a+1,b+1,c+1)
'''
# Nested list
Lis=[[1,2,3],         # name should start with caps letters
     [4,5,6],
     [7,8,9]]

for row in Lis:          #usually use m for row and n for column
    for col in row:
        print(col,end=" ")
    print("\n")
"""
Oprations
1. Addition
2. Multiplication
3. Transposition
4. Scalar Multiplicaion"""
print(Lis)

