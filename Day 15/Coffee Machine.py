Water = 0
Milk = 0
Coffee = 0
Money = 0


def Check_Resources_espresso():
    if Water >= 50:
        pass
    else:
        result = print("Not enough water, please refill.")
        return result, False
    if Coffee >= 18:
        pass
    else:
        result = print("Not enough coffee, please refill.")
        return result, False


def Check_Resources_latte():
    if Water >= 200:
        pass
    else:
        result = print("Not enough water, please refill.")
        return result, False
    if Coffee >= 24:
        pass
    else:
        result = print("Not enough coffee, please refill.")
        return result, False
    if Milk >= 150:
        pass
    else:
        result = print("Not enough milk, please refill.")
        return result, False


def Check_Resources_cappuccino():
    if Water >= 250:
        pass
    else:
        result = print("Not enough water, please refill.")
        return result, False
    if Coffee >= 24:
        pass
    else:
        result = print("Not enough coffee, please refill.")
        return result, False
    if Milk >= 100:
        pass
    else:
        result = print("Not enough milk, please refill.")
        return result, False


print("Welcome to the coffee machine!")
while True:
    print("What would you like? (espresso/latte/cappuccino):")
    user_input = input().lower()
    if user_input == "espresso":
        if Check_Resources_espresso() == None:
            pass
        else:
            continue
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + \
            (nickles * 0.05) + (pennies * 0.01)
        if total >= 1.50:
            print("Here is your espresso ☕️. Enjoy!")
            print(f"Here is ${round(total - 1.50, 2)} in change.")
            Money += 1.50
            Water -= 50
            Coffee -= 18
            continue
        else:
            print("Sorry, that's not enough money. Money refunded.")
            continue
    elif user_input == "latte":
        if Check_Resources_latte() == None:
            pass
        else:
            continue
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + \
            (nickles * 0.05) + (pennies * 0.01)
        if total >= 2.50:
            print("Here is your latte ☕️. Enjoy!")
            print(f"Here is ${round(total - 2.50, 2)} in change.")
            Money += 2.50
            Water -= 200
            Coffee -= 24
            Milk -= 150
            continue
        else:
            print("Sorry, that's not enough money. Money refunded.")
            continue
    elif user_input == "cappuccino":
        if Check_Resources_cappuccino() == None:
            pass
        else:
            continue
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + \
            (nickles * 0.05) + (pennies * 0.01)
        if total >= 3.00:
            print("Here is your cappuccino ☕️. Enjoy!")
            print(f"Here is ${round(total - 3.00, 2)} in change.")
            Money += 3.00
            Water -= 250
            Coffee -= 24
            Milk -= 100
            continue
        else:
            print("Sorry, that's not enough money. Money refunded.")
            continue
    elif user_input == "report":
        print(
            f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}g\nMoney: ${Money}")
        continue

    elif user_input == "off":
        print("Turning off...")
        exit()
    elif user_input == "refill":
        Water = 1200
        Milk = 1000
        Coffee = 500
        Money = 0
        print("Refilling...")
        continue

    else:
        print("Sorry, that's not a valid choice. Please try again.")
        continue
