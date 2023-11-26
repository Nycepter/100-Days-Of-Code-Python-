import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
States_image = "100-Days-Of-Code-Python-/Day 25/US States Game/blank_states_img.gif"
screen.addshape(States_image)
turtle.shape(States_image)
game_on = True
guessed_states = []


States_data = pandas.read_csv(
    "100-Days-Of-Code-Python-/Day 25/US States Game/50_states.csv")

States = States_data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct.", prompt="Enter the name of a state").title()
    if answer_state == "Exit":
        break
    if answer_state in States:
        guessed_states.append(answer_state)
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.penup()
        state_data = States_data[States_data.state == answer_state]
        turt.goto(int(state_data.x), int(state_data.y))
        turt.write(answer_state)


States_missed = []
for state in States:
    if state in guessed_states:
        pass
    else:
        States_missed.append(state)

States_Missed_Export = pandas.DataFrame(States_missed)

States_Missed_Export.to_csv(
    "100-Days-Of-Code-Python-/Day 25/US States Game/Missed States.csv")


screen.exitonclick()
