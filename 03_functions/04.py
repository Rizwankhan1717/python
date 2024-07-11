# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

def circle_stats(raduis):
    area = 3.14 * raduis ** 2
    circum = 2 * 3.14 * raduis
    return area, circum

a , c = circle_stats(3)
print("Area: ",a, "circumference: ",c)