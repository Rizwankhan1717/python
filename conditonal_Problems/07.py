# coffe customization
# Q : customize a coffee order : "Small","Meduim",or "Large" with an option for
#  "Extra Large" of espresso.

coffee_size = str.lower(input("Enter your coffe Size "))
extra_shot = bool(input("With Extra short? "))

if extra_shot == "True":
    coffee = coffee_size + " coffee with extra shot"
else:
    coffee = coffee_size + " coffee"

print(coffee)
