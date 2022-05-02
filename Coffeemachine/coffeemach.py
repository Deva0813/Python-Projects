from replit import clear


def chsMach(choice):

    if choice == 'espresso':
        return MENU['espresso']
    elif choice == 'latte':
        return MENU['latte']
    elif choice == 'cappuccino':
        return MENU['cappuccino']


def acc(q, d, n, p, cost):
    c1 = 0.25*q
    c2 = 0.10*d
    c3 = 0.05*n
    c4 = 0.01*p
    total = c1+c2+c3+c4
    if total > cost:
        balance = total-cost
        return f"\nHere is your {choose}☕ take your balance ${'%.2f' % balance}."

    else:
        return f"\nAmmount Insufficient : Your {choose} cost is ${cost}, So your amount of ${'%0.2f' % total} will be Refunded. "


clear()
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

water = 300
milk = 200
coffee = 100
money = 0
con = 0

while con != 1:

    choose = input("Choose your coffee (espresso / latte / cappuccino) : ")

    if choose == 'report':
        print(
            f"Water : {water}\nMilk : {milk}\nCoffee : {coffee}\nMoney : {money}")
        continue

    choosed_coffee = chsMach(choose)

    water -= choosed_coffee['ingredients']['water']
    milk -= choosed_coffee['ingredients']['milk']
    coffee -= choosed_coffee['ingredients']['coffee']
    money += choosed_coffee['cost']

    if water < 0 or milk < 0 or coffee < 0:
        con = 1
        print("\nSorry due to insufficient amount of ingredients we can't make your coffee, So your money will be refunded.\n")
        continue

    print("\nPlease Insert your coins...\n")

    quarters = float(input("How many Quarters : "))
    dimes = float(input("How many Dimes : "))
    nickles = float(input("How many Nickles : "))
    pennies = float(input("How many pennies : "))

    print(acc(quarters, dimes, nickles, pennies, choosed_coffee['cost']), "\n")
