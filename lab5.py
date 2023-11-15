a="Hello=World=Python"
#sub=a[1:3]   # starts from 1 but 3 means 3-1 i.e 2
#print(sub)
print("\n")
split=a.split("=")
join="-".join(a)
print(split)
print(join)
text="HIIII, BYEEEE "
upper=text.upper()
lstrip=text.lstrip()
rstrip=text.rstrip()
# lstrip() to remove leading whitespace and rstrip() to remove trailing whitespaces
replace=text.replace("BYEEEE","HIIII")
list=text.split(",")
startswith=text.startswith("HIIIi")
endswith=text.endswith("BYEEEE")

print(upper)
print(lstrip)
print(rstrip)
print(replace)
print(startswith)
print(endswith)
print(list)