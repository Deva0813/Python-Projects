from random import choice
from replit import clear
clear()


def random_card():
    """It is used to pick random card."""
    pick_card = []
    for i in range(2):
        pick = choice(card)
        pick_card.append(pick)
    return pick_card


def add_cards(list):
    """It is used to add cards values"""
    add_list = list
    sum1 = 0
    for i in range(len(add_list)):
        sum1 = sum1+add_list[i]
    return sum1


def add_to(per):
    """Make the added value as a single index in list."""
    temp = per
    per = []
    per.append(add_cards(temp))
    return per


def extra(pick):
    pick_card = pick
    pick1 = choice(card)
    pick_card.append(pick1)
    return pick_card


# initial
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
comp_card = []
again = ""
winner = False

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

print(f'''\nYour cards : {user_card}
      
Computer cards : {comp_card}''')

play = input("\nIf you want to hit press 'y' else 'n' for stop.\n")

if play == 'y':
    user_card = random_card()
    comp_card = random_card()

    print(f'''\nYour cards : {user_card}
          
Computer cards : {comp_card}''')

    user = add_cards(user_card)
    comp = add_cards(comp_card)

    # print(user_card, comp_card)

    if user > comp and user >= 21:
        winner = True
        again = "n"
        win = "User"
    elif comp > user and comp >= 21:
        winner = True
        again = "n"
        win = "Compuer"

    if winner == True:
        print(f"\n{win} is the winner...")

    while again != "n":

        again = input("\nDo you want to hit again? (y/n) : ")
        clear()
        print(logo)
        user_card = extra(user_card)
        comp_card = extra(comp_card)
        # print(user_card, comp_card)
        user = add_cards(user_card)
        comp = add_cards(comp_card)
        # print(user, comp)

        print(f'''\nYour cards : {user_card}
              
Computer cards : {comp_card}''')

        if user > comp and user >= 21:
            winner = True
            again = "n"
            win = "User"
        elif comp > user and comp >= 21:
            winner = True
            again = "n"
            win = "Compuer"

        if winner == True:
            print(f"\n{win} is the winner...\n")

else:
    print("Game Over")
