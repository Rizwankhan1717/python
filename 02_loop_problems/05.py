# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character

input_str = str(input("enter the char : "))

for char in input_str:
    if input_str.count(char) ==1:
        print("char is : ",char)
        break
