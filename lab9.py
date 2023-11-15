#print("Even numbers: ")
even=[]
odd=[]
'''for i in range(1,21):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
#print("Even numbers: ")
#print(even)
#print("Odd numbers: ")
#print(odd)
print("\n")
even.extend(odd)
print(even)
print("\n")
#print("Odd numbers: ")
#for i in range(1,21):
    #if(i%2!=0):
        #print(i)
'''
i=1
# using while loop
while(i<=40):
    if(i%2==0 and i<=20):
        print(i)
    if(i%2!=0 and i>20):
        print(i-20)
    i+=1