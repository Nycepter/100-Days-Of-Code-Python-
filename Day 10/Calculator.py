def add(n1, n2):
    print(n1 + n2)
    return (n1 + n2)


def subtract(n1, n2):
    print(n1 - n2)
    return (n1 - n2)


def multiply(n1, n2):
    print(n1 * n2)
    return (n1 * n2)


def divide(n1, n2):
    print(n1 / n2)
    return (n1 / n2)


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'c': "clear"

}
errors = False
reset = True
while True:
    if reset == True:
        try:
            function = operations[f'{input("Enter the symbol for what you would like to do. +, -, *, or /: --> ")}']
            while reset == True:
                try:
                    n1 = int(input("\nWhat is the first number?\n--> "))
                except:
                    print("Invalid input, please try again\n")
                    continue
                while reset == True:
                    try:
                        n2 = int(input("\nWhat is the second number?\n--> "))

                    except:
                        print("Invalid input, please try again\n")
                        continue
                    print("\nThe anser to your input is:")
                    answer = function(n1, n2)
                    print("\n")
                    reset = False

        except:
            print("Invalid input, please try again\n")
    else:
        try:
            function = operations[f'{input("Enter the symbol for what you would like to do with the result. +, -, *, /, or C to clear: --> ").lower()}']
            if function == "clear":
                print("\n")
                reset = True
                continue
            else:
                while reset == False:
                    n1 = answer
                    try:
                        n2 = int(
                            input("\nWhat number would you like to execute the function with?\n--> "))
                    except:
                        print("Invalid input, please try again\n")
                        continue
                    print("\nThe anser to your input is:")
                    answer = function(n1, n2)
                    print("\n")
                    break
        except:
            print("Invalid input, please try again\n")
