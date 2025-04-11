#ASSIGNMENT 01: 

# 01(variable and data type)
print(' \n01)variable and data type\n')
name="Rifat Ahmed"
age=24
is_student=True

# print variable type
print("Name:", name)
print("Type of name:", type(name))

print("Age:", age)
print("Type of age:", type(age))

print("Is Student:", is_student)
print("Type of is_student:", type(is_student))


# 02(arithmetic operation)
# my age 24 and let, any number a=6
print("\n2) arithmetic operation\n")
age=24
print("age=",age)
a=6
print("any number : a= ",a)
print("multiplication: ",age*a)
print("summation: ",age+a)
print("division: ",age/a)
print("substruction: ",age-a)

#comparision operator
print("\n3)comparision operator\n")
age=24
print("is age > 18 : ",age>18)
print("is age == 18 : ",age==18)
print("is age <= 18 : ",age<=18)

#logical operator
print("\n4)logical operator\n")
x=5
y=10
z=7
print(x>0 and y<9)
print(x>0 or y<9)
print(not(x>0 and z<9))

#assignment operator
print("\n5)Assignment operator\n")

x=10
x+=2
print(" x+2= ",x)

x-=2
print(" x-2= ",x)

x*=2
print(" x*2= ",x)

x/=2
print(" x/2= ",x)

#identity operator
print("\n6)identity operator\n")
a = 5
b = 6
print("a=",a)
print("b=",b)

print("a is b:", a is b)                     
print("a is not b:", a is not b)


#membership operator
print('\n07) membership operator \n')

lst=["arif vaiya","rifat","rahat"]

print("arif vaiya in list : ","arif vaiya" in lst)

print("pintu not in list : ","pintu" not in lst)