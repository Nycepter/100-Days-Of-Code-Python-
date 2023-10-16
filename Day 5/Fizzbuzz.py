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
