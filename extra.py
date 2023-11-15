my_list=[1,2,3,4,5,6]
def change_value(my_list):
    my_list[3]=5
    my_list[4]=4
    print("\nValue in the list:",my_list)
    print("Address:",id(my_list))
    return 
print("\nBefore function call,list:",my_list)
print("Address:",id(my_list))
print("\nAddress:",id(my_list[3]),id(my_list[4]))
change_value(my_list)
print("\nAfter function call,list:",my_list)
print("Address:",id(my_list))
print("Address:",id(my_list[3]),id(my_list[4]))

# print("Address:",id(my_list),end="\n\n")
# print("Address:",id(my_list[3]),sep="\n")
# end=" " by default it returns \n and we can change that as per our choice
# sep=" " by default it returns a space ' ' we can also change that as per our choice
# or we can just use print("\n")

# list - memory is allocated dynamically
# thus a single address is allocated for a whole list but individual addresses of the elements are different 
# list is mutable
# even if an element is changed the address of the whole list remains same
# changing an element results in change in the address of that element
# the size is not an issue
# and sometimes it can be a disadvantage as well