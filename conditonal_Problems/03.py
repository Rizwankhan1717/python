# Grade Calculator 
# Q : Assign a leeter grade based on a Student's score : A(90-100), B(80-89),
#     C(70-79),D(60-69), F(below 60)

Score = int(input("Enter your Score : "))
if Score >= 101 :
    print("please verify your grade again")
    exit()

if Score >= 90 :
    print("Grade A ")
elif Score >= 80 :
    print("Grade B")
elif Score >= 70 :
    print("Grade C")
elif Score >= 60 :
    print("Grade D")
else:
    print("Grade F")