for Number in range(1, 101, 1):
    if Number % 3 == 0 and Number % 5 == 0:
        print("FizzBuzz")
        continue
    elif Number % 5 == 0:
        print("Buzz")
        continue
    elif Number % 3 == 0:
        print("Fizz")
    else:
        print(Number)


for Number in range(1, 101, 1):
    output = ""
    if Number % 3 == 0:
        output += "Fizz"
    if Number % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(Number)
    print(output)
