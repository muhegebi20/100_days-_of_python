logo = '''

 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''

def calculator():
    print(logo)
    first = float(input("what's the first number?: ").strip())
    M_operators = ["+", "-", "*", "/"]
    def add(a, b):
        return a+b
    def multiply(a,b):
        return a*b
    def devide(a,b):
        return a/b
    def substruct(a,b):
        return a-b
    calc_continue = True
    while calc_continue:
        result = 0
        for o in M_operators:
            print(o)
        operator = input("Pick an operation: ").strip()
        while operator not in M_operators:
            operator = input("Pick an operation: ").strip()
        sec = float(input("what's the next number?: ").strip())
        operations = {
        "+": add,
        "-": substruct,
        "*": multiply,
        "/": devide
        }
        result = operations[operator](first,sec)
        print(f"{first} {operator} {sec} = {result}")
        contin = input(f"Type 'y' to continue calculating with {result}, or type n for new calculation: ").strip()
        if contin != "y":
            calc_continue = False
            print("\n"*20)
            calculator()
        else:
            first = result

calculator()