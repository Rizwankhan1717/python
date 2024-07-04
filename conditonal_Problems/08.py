# password Strenght Checker 
# Q : Check if a Password is "Weak","Meduim",or "Strong". 
# Criteria : < 6 chars (weak), 6-10 chars (Meduim), > 10 (String.)

password = str(input("Enter your Password : "))

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10 :
    strength = "Meduim"
else:
    strength = "Strong"

print("password Strength is ",strength)