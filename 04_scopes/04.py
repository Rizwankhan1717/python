def func(num):
    def actual(x):
        return x ** num
    return actual

f = func(2)
g = func(3)

print(f(2))
print(f(3))