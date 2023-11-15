# Default values 
# Evaluated only once

def func(a="L",b=90):
    print("Value of a: ",a)
    print("Value of b: ",b)
    return
func(a="Monika",b=50)
func(a="Lalit")
func(b=30)
func()

# No need to write 'a'= ? and 'b'=? to assign the values
# By default the 1st argument will be passed to the 1st parameter and so on
# func(a="Monika",b=50) can be written as func("Monika",50)
# func(a="Lalit") and in this case b wasn't assigned so the default value will be considered