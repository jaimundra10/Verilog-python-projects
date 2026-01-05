This project teaches:
- functions  
- loops  
- if/else  
- dictionaries  
- simple logic  

Easy to read. Easy to understand. Great for learning Python.
*************************************************************************************************
Menu = {
"Espresso": {
    "ingredients": {
        "water" : 50,
        "coffee": 18,
    },
    "cost":1.50,
},

"Cappuccino": {
    "ingredients": {
        "water" : 250,
        "coffee": 24,
        "milk":100,
    },
    "cost":3.00,
},

"Latte": {
    "ingredients": {
        "water" : 200,
        "coffee": 24,
        "milk":150,
    },
    "cost":2.50,
}
}
profit = 0
cup_sold = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Coin = {
    "Penny" : 0.01,
    "Dime" : 0.10,
    "Nickel" : 0.05,
    "Quarter" : 0.25,
}

def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry we don't have enough {item} to make")
            return False
    return True


def coins():
    print("paise daal bc")
    p, d, n, q = map(int, input("Penny Dime Nickel Quarter: ").split())
    return p*0.01 + d*0.10 + n*0.05 + q*0.25



def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit, cup_sold
        profit += drink_cost
        cup_sold += 1

        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink,ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]
    print(f"here is your {drink}")

is_on = True

while is_on:
    order = input("What would you like to order (espresso/cappuccino/latte)?\n").capitalize()
    if order == "off":
        is_on = False
        print("machine is turned off now")
        break
    elif order == "Report":
        print(f"Water remaining {resources['water']}")
        print(f"Milk remaining {resources['milk']}")
        print(f"Coffe remaining {resources['coffee']}")
        print(f"Money: ${profit}")
        print(f"Cups sold: {cup_sold}")
        continue
    elif order not in Menu and order !="Report":
        print("bk sahi order daal")
    else:
        coffee = Menu[order]
        if enough_resources(coffee["ingredients"]):
            payment = coins()
            if is_transaction_successful(payment,coffee["cost"]):
                make_coffee(order,coffee["ingredients"])







