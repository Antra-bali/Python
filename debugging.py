
# 4.
def a(num):
    if num>0:
        return "Positive"
    elif num==0:
        return "Zero"
    else:
        return "Negative"
    
b=a(0)
print(b)

# 1.
def find_avg(numbers):
    total=0
    for num in numbers:
        total+=num
    return total/len(numbers)
nums=[10,20,30]
avg=find_avg(nums)
print(avg)