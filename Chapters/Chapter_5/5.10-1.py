# 5.10 Logical Opposites

# Bad usage of not operator

age = int(input("Enter your age: "))

if not (age >= 17):
    print("You're not old enough")

# Using logical opposites

if age <= 17:
    print("You're not old enough")
else:
    print("Congratulations, you qualify for a free iPhone!")

sword_charge = int(input("Define your sword charge: "))
mana_charge = int(input("Define your mana charge: "))

def kill_dragon():
    if (sword_charge <= 90) and (mana_charge <= 80):
        print("The dragon has killed you")
    else:
        print("You have slayed the dragon.")
kill_dragon()