import prettytable
from prettytable import PrettyTable
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()

my_menu = Menu()

my_coffee_maker = CoffeeMaker()

is_on = True
while is_on == True:
    options = my_menu.get_items()
    selection = input(f"What would you like? {options}\n")
    if selection == "off":
        is_on = False
    elif selection == "report":
        my_coffee_maker.report()
        my_money_machine.report()
        continue
    else:
        pass

    order = my_menu.find_drink(selection)
    if order == None:
        continue

    has_resources = my_coffee_maker.is_resource_sufficient(order)
    if has_resources == False:
        continue

    if my_money_machine.make_payment(order.cost) == False:
        continue
    my_coffee_maker.make_coffee(order)
