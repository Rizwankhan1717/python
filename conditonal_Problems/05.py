# Weather activity suggestion 
#  Q : suggest an activity based on the weather(e.g: sunny - go for walk, Rainy -read a book,Snowy-build a snowman)

weather = str.lower(input("Enter today's weather : "))

if weather == "sunny":
    activity = "go for the Walk"
elif weather == "rainy" :
    activity = "Read a book"
elif weather == "snowy":
    activity ="Build a snow man"

print(activity)