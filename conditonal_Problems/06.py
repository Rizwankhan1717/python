#  Trasportation Mode Selection
# Q : Choose  a mode of transportation based on the distance (e.g. <3 : walk, 3-15km : bike, >15 : car)

distance = int(input("Enter the Distance : "))

if distance < 3 :
    transport = "Walking"
elif distance <= 15 :
    transport = "Bike"
else:
    transport = "Car"

print("we recommends you the  ",transport)