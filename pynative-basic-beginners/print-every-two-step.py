# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


def print_every_two(string_given):
    listed_string = list(string_given)
    print(listed_string)

string_input = input("please wright a word: ")
print_every_two(string_input)
