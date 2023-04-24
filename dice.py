import random
sides=int(input("Please enter the number of sides on the die."))
while True:
    roll=input("Would you like to roll the die?")
    theroll=random.randint(1,int(sides))
    print(theroll)