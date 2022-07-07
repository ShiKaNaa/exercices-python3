# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse.
# For example 545, is the palindrome numbers

import math

def check_if_palindrome(user_number):
    # mettre le int dans une list et le split
    list_of_num = math.ceil(user_number)
    print(list_of_num.split())
    # verrifier si list[n] == list[-n]
    return True

# user_input = int(input("please enter a number: "))
print(check_if_palindrome(454))
print(check_if_palindrome(13331))
print(check_if_palindrome(1661))
print(check_if_palindrome(14599541))

print(check_if_palindrome(1231))
print(check_if_palindrome(16429815641))
