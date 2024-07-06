# Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

input_num = int(input("Enter the number : "))
factorial = 1

while input_num > 0:
    # factorial = factorial * input_num
    factorial *= input_num
    # input_num = input_num - 1
    input_num -= 1

print("Factorial of num is : ",factorial)


