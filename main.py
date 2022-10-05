from tkinter import Menu

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def resources_sufficient(order_resources):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_resources:
        if order_resources[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


coffee_machine_on = True

while coffee_machine_on == True:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == "report":
        for resource in resources:
            print(resource, ":", resources[resource])
        print(f"Money: ${profit}")
    elif user_order == 'off':
        coffee_machine_on = False
    else:
        drink = MENU[user_order]
        if resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_order, drink['ingredients'])
