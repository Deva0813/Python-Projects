from replit import clear #import replit from pip install replit

def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mul(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


oper = {"+": add,
        "-": sub,
        "*": mul,
        "/": div}

clear()
# con = 0
# while True:


def calculator():
    print("""
    _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
    |_____________________|
    """)
    f_num = int(input("Enter first number : "))
    rep = ""
    while rep != "n":

        op = input(
            "\nChoose the operation you want to perform ( + , - , *, / ) : ")
        l_num = int(input("\nEnter the last numebr : "))
        print(f"\n{f_num} {op} {l_num}\n")

        # if op == '+':
        #     ans = add(f_num, l_num)
        #     print(ans)
        # elif op == '-':
        #     ans = sub(f_num, l_num)
        #     print(ans)
        # elif op == '*':
        #     ans = mul(f_num, l_num)
        #     print(ans)
        # elif op == '/':
        #     ans = div(f_num, l_num)
        #     print(ans)
        # else:
        #     print("Invalid operator...")

        func = oper[op]
        print(func(f_num, l_num))
        ans = int(func(f_num, l_num))
        rep = input(
            f"""\nDo you want to perform any other operation with {ans},
                
if yes type 'y' else if you want to continue with new one type 'n' : """)
        f_num = ans
        if rep == "y":
            continue
        else:
            rep = "n"
            clear()
            calculator()


calculator()
