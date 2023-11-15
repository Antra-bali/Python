# all() - Returns True if all elements in an iterable are true, otherwise returns false
list1= [True,True,True]
list2= [True,False,False]
print(all(list1))
print(all(list2))

# any() - Returns True if any element in an iterable is true, otherwise returns false
list3= [False,False,False]
list4= [True,False,False]
print(any(list3))
print(any(list4))

# ascii() - Returns a string containing a printable representation of an object.
# It is used to get a printable representation of an object, not its ASCII value
print(ascii("Kot, \nBhalwal!"))   # \n is also considered an object

# The ord() function returns the Unicode code point of a character
# which is a more comprehensive character encoding than ASCII
print(ord("a"))
print(ord(" "))
print(ord(","))
print(ord("*"))
print(ord("0"))
print(ord("5"))

# bin() - Converts an integer to a binary string.
print(bin(10))     # 0b is defined (literal)
print(bin(15))


# bool() - Converts a value to a Boolean (True or False)
print(bool(0))
print(bool(42))
print(bool([]))
print(bool([1,2]))

# b is a literal in case of bytes and it is returned without fault

# bytearray() - Returns a mutable bytearray object from an iterable of integers
byte_array= bytearray([65,66,67])
print(byte_array)
byte_array[0]= 88 # ASCII value for 'X'
print(byte_array)

# bytes() - Returns an immutable bytes object from an iterable of integers
byte_string= bytes([68,69,70])
print(byte_string)

# callable() - Returns True if the object appears callable (can be called as a function), false otherwise
def func():
    return 42
print(callable(func))
print(callable(42))