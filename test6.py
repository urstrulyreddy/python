#test3.py
a=5
b=2.3
c=2+3j
d=b>a
print(type(a))
print(type(b))
print(type(c))
print(type(d))
b=complex(a,c)
c=int(a)
print(a)
print(b)
print(c)
print(d)
list=[1,2,3,4]
print(type(list))
print(list)
tuple=(5,6,7,8) #tuple doesnt support item assignment
print(type(tuple))
print(tuple)
set={9,0,1,2}
print(type(set))
print(set)
num = 7
amt=123.45
code='A'
pi = 3.1415926536
population_of_India=1000000000
msg = "hi"

print("num="+str(num))
print("\n amt="+str(amt))
print("\n code="+str(code))
print("\n population="+str(population_of_India))
print("\n message="+str(msg))