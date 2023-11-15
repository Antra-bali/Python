# create 5 students record
# name = , roll number=, record=,
# append this in list
# and add search method
stu={}

#input('Enter the roll number of the student you want to check the record of: ')


# a function to create the student record
def record():
    roll=int(input("Enter the roll number: "))
    name=input("Enter the name: ")
    marks=input("Enter the marks: ")
    stu[roll]=[name,marks]

def search():
    re=int(input('Enter the roll number of the student you want to check the record of: '))
    if re in stu.keys():
        print('Name: ',stu[re][0])
        print('Roll number: ',re)
        print('Marks: ',stu[re][1])
    else:
        print('Roll number not found')

ch=0
while(1):
    ch=int(input('Enter your choice: '))
    if ch==1:
        record()
    elif ch==2:
        search()
    elif ch==3:
        break
    else:
        print("Invalid Choice")
        



