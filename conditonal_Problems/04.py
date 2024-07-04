# Fruit Ripeness checker
# Q : Determine if a fruit is ripe,overripe,or unripe based on its color
#     eg: banana : Green- Unripe, Yellow-Ripe , Brown-Overripe)

fruit_condi = str(input("Enter your Fruit condition : "))

if fruit_condi == "green" :
    print("Unripe")
elif fruit_condi == "yellow" :
    print("Ripe")
else:
    print("overripe")