from turtle import Turtle, Screen
import prettytable
from prettytable import PrettyTable


# Turtley = Turtle()
# Turtley.shape("turtle")
# Turtley.color("chartreuse4")
# Turtley.forward(100)


# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()


Table = PrettyTable()
Table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
Table.add_column("Type", ["Electric", "Water", "Fire"])
Table.align = "l"
print(Table)
