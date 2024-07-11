# example : this is example global variable can access inside the function
x = 90 

def func(y):
    z = x * y
    return z

result = func(10)
print(result)