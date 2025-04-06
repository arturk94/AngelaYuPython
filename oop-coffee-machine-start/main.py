from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cm.report()
        mm.report()
    else:
        mi = m.find_drink(choice)
        is_enough_ingredients = cm.is_resource_sufficient(mi)
        is_payment_successful = mm.make_payment(mi.cost)
        if is_enough_ingredients and is_payment_successful:
            cm.make_coffee(mi)






