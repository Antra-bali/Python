'''# 3x3 matrix
print("\n")
Matrix=[]
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
K=int(input('Enter the row to reverse: '))
for i in range(r):
    row=[]
    for j in range(c):
        h=int(input())
        row.append(h)
    if (i+1)%K == 0:
        Matrix.append(list(reversed(row)))
    else:
       Matrix.append(row)
        #Matrix.append(i,j)
print(Matrix)
'''
Final=[]
'''for i, ele in enumerate(Matrix):
    if (i+1)%K == 0:
        Final.append(list(reversed(ele)))
    else:
        Final.append(ele)
print("Final matrix: ",Final)'''

r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
K=int(input('Enter the row to reverse: '))
for i in range(r):
    row=[]
    for j in range(c):
        h=int(input())
        row.append(h)
    Final.append(row)
print(str(Final))
r=[]
for i,j in enumerate(Final):
    if(i+1)%K==0:
        r.append(list(reversed(j)))
    else:
        r.append(j)
print(r)

'''test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2],
            [3, 6], [3, 7, 4], [2, 9]]
print("The original list is : " + str(test_list))
K=int(input('Enter the row value want to reverse'))

res = []
for idx, ele in enumerate(test_list):
    if(idx + 1) % K == 0:

        res.append(list(reversed(ele)))
    else:
        res.append(ele)
print("After reversing every Kth row: " + str(res))
'''
