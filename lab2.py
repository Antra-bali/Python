# Python Program for Creation of String

# Creating a String with Single Quotes
Str1='Hello, this is a single-quoted string'
print("String with the use of Single Quotes:")
print(Str1)

# Creating a String with Double Quotes
Str2="Python is my favorite programming language"
print('\nString with the use of Double Quotes:') # can use either "" or''
print(Str2)
print(type(Str2)) # print the data type of string 2
print(type(Str1)) # print the data type of string 1

# Creating a String with Triple Quotes
Str3='''This is a triple-quoted string
that spans across multiple lines.
It can include ' single' and " double" quotes without escaping.'''
print('''\nString with the use of Triple quotes:''')
print(Str3)
print(type(Str3)) # print the data type of string 3

# Creating a String with Triple Quotes allows multiple lines
Str4='''Strings
can
be
multiline'''
print('''\nCreating a multiline string:''')
print(Str4)

# Concatenating two Strings
Str5 =Str1+''' and '''+Str2
print("\nConcatenated Strings:\n")
print(Str5)