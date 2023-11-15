ages=[1,2,3]
print(ages)
print(ages[2])
print(ages[-3])
print(ages[0])
list=['a','b','c','d','e','f','g','h']
print(list[2:5])
print(list[5:])
print(list[:])
print("\n")

# append() adds an item at the end of the list
num=[21,54,34,23]
print("Before:",num)
num.append(20)
print("After:",num)
print("\n")

# extend() adds all the items of an iterable to the end of the list
# or adds the two lists
n=[1,3,5]
even=[2,4,6]
n.extend(even)
print("List after append:",n)
print("\n")

# insert() adds an element at the specified index
numbers=[10,20,30,40]
numbers.insert(1,100)
print(numbers)

# change list items 
lang=['Japanese','Chinese','Spanish','Persian']
lang[3]='English'
print(lang)

# try replace() 
# function doesn't work but can use normally index to replace an item
r=[3,6,2,7]
print("Before:",r)
r[3]=5
print('After:',r)

# Removing an element using delete // del
print("\n")
langg=['C','C++','Python','Swift',"R"]
# deleting index based
del langg[3]
print(langg)
# deleting the last element
del langg[-1]
print(langg)
# deleting the first two elements
del langg[0:2]
print(langg)

del langg[2:4:2]
print(langg)
print("\n")

# removing the elements
remove=['C','B','G']
remove.remove('C')
print(remove)

# trying range in loops
print("\n")
listcheck=[21,11,2003,25,12,1,6,1,5,7]
print(listcheck)
for i in range(0,10):      # range works in this case from 0 to 10-1 so 9
    print(listcheck[i])
print("\n")
size=len(listcheck)-1
for i in range(size,-1,-1):   # size is for the last element of the list // -1 for reverse order // -1 for the first item
    print(listcheck[i])