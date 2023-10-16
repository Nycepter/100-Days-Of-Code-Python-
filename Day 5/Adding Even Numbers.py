"""

Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.
"""
Total = 0
Target = int(input("Enter your number here. \n"))
Target_List = []
while True:
    if Target == 0:
        for Number in Target_List:
            Total += Number
        print(
            f"{Total}")
        break

    elif Target % 2 == 0:
        if Target > 0 and Target < 1000:
            Target_List.append(Target)
            Target -= 2
            continue
        else:
            print("Your number is too big or too small. Please try again.")
            break

    elif Target % 2 != 0:
        if Target > 0 and Target < 1000:
            Target -= 1
            continue
        else:
            print("Your number is too big or too small. Please try again.")
            break
    else:
        print("error")
        break


# for Number in range("Starting Number", "Ending Number", "Increment Value"):
# In the code below, we start at 2 and go to the input -input of 100 would be 1-99 so we add 1 to include 100-, then increment the number by 2 so that we keep the numbers adding even only.

Target = int(input("Enter your number here. \n"))
Total = 0
for Number in range(2, Target + 1, 2):
    Total += Number
print(Total)
