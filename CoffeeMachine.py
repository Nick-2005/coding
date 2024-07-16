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
    },
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report_data():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: {profit} $")

def is_successful_resource(ingredients):
    for i in ingredients:
        if ingredients[i]>resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def process_coins():
    print("Please insert coins")
    total = int(input("How many quaters: "))*0.25
    total += int(input("How many dimes: "))*0.1
    total += int(input("How many nickels: "))*0.05
    total += int(input("How many pennies: "))*0.01
    return total

def is_transaction_successful(money,drink):
    if money >= drink:
        change = round(money-drink,2)
        print(f"here is ${change} in change")
        global profit 
        profit += drink
        return True
    else:
        print("Sorry not enough money . Money Refunded")
        return False
def make_coffee(drink,order):
    for i in order:
        resources[i] -= order[i]
    print(f"Here is your {drink}. Enjoy!!")


def machine():
    is_on = True
    while is_on:
        user = input("What would you like(espresso/latte/cappuccino): ").lower()
        if user == "report":
            report_data()
        elif user == "off":
            is_on = False
        elif user == "espresso" or user == "latte" or user == "cappuccino":
            drink = MENU[user]
            if is_successful_resource(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment,drink['cost']):
                    make_coffee(user,drink['ingredients'])

            
        
            
machine()