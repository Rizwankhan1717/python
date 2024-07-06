# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True: 
    number = int(input("Enter the number btw 1 to 10 : "))
    if 1 <= number <= 10:
        print("correct number")
        break
    else:
        print("invalid number, try gain")