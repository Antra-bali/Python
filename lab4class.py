# Passing of immutable arguments
# Integer

a=10
def change_value(a):
    a=20
    print("Inside Function,address:",id(a))
    return a

print("Before function call,a=",a,"Address:",id(a))
a=change_value(a)
print("After function call,a=",a,"Address:",id(a))

#b=change_value(a)
#print("After function call,a=",a,"Address:",id(a))
#print("After function call,b=",b,"Address:",id(b))

# basically we are rewriting the value of 'a' with the function call thus printing the same address as in the function