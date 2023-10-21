"""
1
2
3
4
5
6
7
8
9
10
11
# Write your code below this line 👇





# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
1
13
Evaluation

0:02

1:33

SLIDE 1/2
Description

Send Feedback

Instructions
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Prime number graphic

Here are the numbers up to 100, prime numbers are highlighted in yellow:

First 100 Primes

Example Input 1
73
Example Output 1
It's a prime number.
Example Input 2
75
Example Output 2
It's not a prime number."""


# Write your code below this line 👇
def prime_checker(number):
    prime = 0
    for num in range(2, number):
        if number % num == 0:
            prime += 1

    if prime > 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
