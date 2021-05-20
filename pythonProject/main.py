# OOP's Concept :-
# turtle = module
# Turtle, Screen = class
# timmy = object
# shape, color = attributes

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Packages
# prettytable = package
# PrettyTable = class
# table = object created
# add_column = method

import prettytable as p             # Alias

table = p.PrettyTable()
table.add_column("Artists", ["Taylor", "Eminem", "Jay-Z"])
table.add_column("Grammys won", [10, 15, 20])

print(table)
