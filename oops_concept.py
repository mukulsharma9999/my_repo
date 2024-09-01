'''a,b=10,5
if (a>b):
    print("a is smaller than b")
else:
    print("b is smaller than a ")'''

# find the maximum of two numbers
'''def maximum(a, b):
    if a>b:
        return a
    else:
        return b
a,b=3,4
print(maximum(a,b ))'''

# find maximum using ternary opreator
'''num1 = int(input("Enter your first number :"))
num2 = int(input("Enter your Second number :"))
print("The maximum of all values is ", (num1 if num1>=num2 else num2))

value_odd = int(input("Enter your given value :"))
result = "Even" if value_odd % 2==0 else "odd"
print(result)'''


#more real life examples of ternary opreator 
# it is use in the conditional opreator to consize the code
user_age = int(input("Enetr your age :"))
aces_level = "Admin" if user_age>= 18 else "Guest"
print("user aceess level :", aces_level)

