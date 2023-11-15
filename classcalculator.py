class Cal:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
    def sub(self):
        return self.n1-self.n2
    def mul(self):
        return self.n1*self.n2
    def div(self):
        return self.n1//self.n2
a=int(input('Enter first number: '))
b=int(input('Enter second number: ')) 
print("Enter \n1. for Addition\n2. for Subtraction\n3. for Multiplication\n4. for Division\n5. for Exit")
while(1):
    c=int(input('Enter your choice: '))
    if c==1:
        Add=Cal(a,b)
        print(Add.add())
    elif c==2:
        Sub=Cal(a,b)
        print(Sub.sub())
    elif c==3:
        Mul=Cal(a,b)
        print(Mul.mul())
    elif c==4:
        Div=Cal(a,b)
        print(Div.div())
    elif c==5:
        break
    else:
        print("Invalid choice")