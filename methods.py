"""
LIST METHODS
Methods    Description
append()   add an item to the end  of the list
extend()   add all the items of an iterable to the end of the list
insert()   inserts an item at the specified index
remove()   removes item present at the given index
pop()      returns and removes item present at the given index
clear()    removes all items feom the list
index()    returns the index of the first matched item
count()    returns the count of the specified item in the list
sort()     sort the list in ascending/descending order
reverse()  reverse the item of the list
copy()     returns the shallow copy of the list
""" 
list=[1,2,2,2,3,4,4,4,5]
print(list.count(2))
list.sort()
print(list)
print(list.pop(4))
print(list)
list.clear()
print(list)


