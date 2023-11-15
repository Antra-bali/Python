# TUPLE
# A tuple can have any number of items  and they may be od different types(integer,float,list,string,etc)
# Immutable // can not modify
# Different types of tuples

# Empty tuple
tuple=()
print(tuple)
print("\n")

# Tuple with mixed data types
tuple=(1,'Hello',3.4)
print(tuple)
print("\n")

# Nested tuple
tuple=('Mouse',[1,2,3],(1,2,3))
print(tuple)
print(type(tuple[0]))    # To check the type of the items of tuple use index
print(type(tuple[1]))
print(type(tuple[2]))
print("\n")

#Tuple with one Element
v1=('Hello')
v2=('Hello',)
print(type(v1))
print(type(v2))
print("\n")

'''
Access Python Tuple Elements
1. Indexing
2. Slicing
'''
# 1. Iterating through a Tuple in Python
lang=('Python','Swift','C')
for language in lang:
    print(language)
print("\n")

# 2. Check if an Item Exists in the Python Tuple
lang=('Python','Swift','C')
print('C'in lang)
print('V' in lang)