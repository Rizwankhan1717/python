# 2Q : movie ticket pricing :
#      movie ticket are priced based on age : $12 for Adult (18 and over),8$ for children 
#      everyone gets a 2$ discont on wednesday \

age = int(input("Enter your age : "))
day = str(input("Today's Date : "))

price = 12 if age >=18 else 8
if day == "Wednesday" :
    price -= 2 
print("Tickect price for you is $",price)

