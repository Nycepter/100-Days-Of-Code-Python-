"""

---Instructions---
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

The last line of your program should print the result.

"""

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇


print(int(two_digit_number[0]) + int(two_digit_number[1]))

"""
input takes the two numbers and returns them as a string. 

24 is output as "24" 

We use two_digit_number[0] to access the first number and two_digit_number[1] to access the second number

but they are both still string elements, so if they are added together then you would just get "24" still. 

we can fix this by converting each to an integer when we pull the data. To do this we and int() and place the call in the parenthesis.

this will return each as a number so that they can be added together mathematically. Returning 2 + 4 = 6.


--------
#my code
--------

two_digit_number = input()
print(int(two_digit_number[0]) + int(two_digit_number[1]))

-------------
#given answer
-------------

two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit

print(two_digit_number)

"""
