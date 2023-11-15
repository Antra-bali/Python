a={'Name':'Antra','Age':23,'City':'Kyoto','Current city':'Jammu'}
# can also initialize an empty dictionary 
# a={}
# and append the keys and values
a['anything']='something'
print("\n")
a['Dislikes']='People'
del a['Current city']
print(a)
print("\n")
# to print a specific value
print(a['Age'])
'''print("\n")
a={}
a['Alice']=92
a['Bob']=85
a['Charlie']=78
a['David']=95
a['Eve']=88
print(a)
#b=max(a.values())
max=0
for i in a:
    if max<a[i]:
        max=a[i]
print(max)
for i in a:
    if a[i]==max:
        print(i)
print("\n")
dict={}
dict['a']=10
dict['b']=20
dict['c']=30
print(dict)
m=0
for i in dict:
    if m<dict[i]:
        m=dict[i]
print(m)
# i'''