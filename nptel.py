s='Hello Everyone'
print(s.lower())

a=['','h','e','l','','l','o']
print('.'.join(a))
print("\n")

b='The joy of Computing'
b=b.replace('a','_')
b=b.replace('e','_')
b=b.replace('i','_')
b=b.replace('o','_')
b=b.replace('u','_')
print(b)
print("\n")

x='The Joy of Computing'
print(x[3:12])
print("\n")

A='Sheher mein'
z='aeiouAEIOU'
for i in range(len(A)):
    if(A.index(A[i])%2==0):
        print(i)
        if(A[i] in z):
            A=A.replace(A[i],'_')

print(A)
print("\n")

import numpy as np
a=np.array([[8,9,20],[10,31,22]])
b=np.array([[1,2,3],[4,5,6]])
print(a-b)

import numpy as np
b=np.array([[1,2],[3,4]])
print(np.sum(b,axis=1))