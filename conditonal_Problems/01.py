# 1Q : age group categorization : classify a person's age group :
#      child (<13),teenager(13-19),Adult(20-59),senior(60+)

User_age = int(input("Enter Your Age :"))

if User_age < 13 :
    print("child")
elif User_age < 20 :
    print("Teenager")
elif User_age < 59 :
    print("Adult")
else : 
    print("Senior")


 