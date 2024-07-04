# pet food recommendation 
# Q : Recommendd a type of pet food based on the pets species and age 
#     e.g dog: <2 years - puppy food, cat - senior cat food.

pet = str.lower(input("Enter your pet name : "))
pet_age = int(input("Enter your pet age : "))

if pet == "dog" :
    if pet_age < 2:
        print("Puppy food")
    else:
        print("snr dog food")

if pet == "cat" :
    if pet_age < 5:
        print("junior catfood")     
    else :
        print("senior cat food")
    


