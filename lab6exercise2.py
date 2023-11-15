'''
Imagine having a dataset containing information about students. Each student's data is represented as a tuple
Student ID
Name
Age
Gender
List of subjects

Create a list of student tuples with at least 5 entries
Function that calculates and returns the average age of all students
Function that finds and returns the student with the most subjects enrolled
Function that finds and returns the student with the fewest subjects enrolled

'''
student=[(1,"A",10,'Fe',('M','S','J','K')),(2,'B',11,'Male',('M','CS','B')),(3,'C',12,'Fe',('M','S','J','K','C','A')),(4,'D',13,'Male',('M','S','B')),(5,'E',14,'Fe',("M",'K','A'))]

# function that calculates and returns the average age of all students
def avg_age(student):
    avg=sum(students[2]for students in student)/len(student)
    return avg
print('Average age of all the students: ',avg_age(student))

# Function that finds and returns the student with the most subjects enrolled
# def most_sub(student):

