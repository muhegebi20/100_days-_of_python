from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

r_menu = Menu()
coffemaker = CoffeeMaker()
machine = MoneyMachine()

closeMachine = False
while not closeMachine:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order in r_menu.get_items().split("/"):
        order = r_menu.find_drink(order)
        print(f"{order.name} is ${order.cost}")
        if coffemaker.is_resource_sufficient(order):
            isAccepted = machine.make_payment(order.cost)
            if isAccepted:
                coffemaker.make_coffee(order)
    else:
        if order == "report":
            coffemaker.report()
            machine.report()
        else:
            closeMachine = True
    
