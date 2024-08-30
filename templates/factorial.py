def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result
number = int(input("enter your number :"))
print('factorial of', number,'is',factorial(number))