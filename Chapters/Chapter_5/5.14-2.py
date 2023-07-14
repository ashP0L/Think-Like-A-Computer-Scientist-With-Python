# 2. You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving
# on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general
# version of the program which asks for the starting day number, and the length of your
# stay, and it will tell you the name of day of the week you will return on.

days = [0, 1, 2, 3, 4, 5, 6, 7]
days[1] = "Monday"
days[2] = "Tuesday"
days[3] = "Wednesday"
days[4] = "Thursday"
days[5] = "Friday"
days[6] = "Saturday"
days[7] = "Sunday"

def number_of_days(totaltime,startday):
    """Performs calculations for day of arrival"""
    x = startday +(totaltime % 7)
    if (x > 7):
        y = x-7
        print(y)
        print("You will arrive home on a", days[y])
    else:
        print("You will arrive home on a", days[x])

def mainloop():
    start_day_input = int(input(" \nThis program calculates which day you will arrive home.\n\nChoose the day of your departure:\n\t 1: Monday\n\t 2: Tuesday \n\t 3: Wednesday \n\t 4: Thursday \n\t 5: Friday \n\t 6: Saturday \n\t 7: Sunday \n"))
    #type safety
    if start_day_input == type(int):

    startday = days[start_day_input]
    nights = int(input("How many nights is your stay? \n"))

    number_of_days(nights, start_day_input)

mainloop()


