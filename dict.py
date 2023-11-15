a = {'key1': 1, 'key2': 2, 'key3': 3}
print("\n")
for i in a:
    print(i)                  # for printing keys
for i in a.values():
    print(i)                  # for printing values and using for loop to access a single element at a time
print(a.values())             # this will print the whole values
print("\n")
for i, j in enumerate(a.items()):
    print('keys',i,'values',j)
    print(a.items())
print("\n")
for i, j in a.items():
    print('keys',i,'values',j)
    print(a.items())
print("\n")
print(a.keys())
print(a.values())
print(a.items())