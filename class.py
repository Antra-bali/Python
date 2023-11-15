# first letter should be caps
class Adder:
    def __init__(self,n1,n2):    # syntax 2 underscore
        self.n1=n1
        self.n2=n2           #n1,n2 are attributes

    def add(self):
        return self.n1+self.n2
a=int(input())
b=int(input()) 
# creating an object
Addition=Adder(a,b)
result=Addition.add()
print(f"sum of {Addition.n1} and {Addition.n2} is {result}")
print("Sum of",Addition.n1,"and",Addition.n2,"is",result)