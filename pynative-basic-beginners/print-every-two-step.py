# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

string_input = input("please wright a word: ")
every_two_elements = string_input[0::2]
print(every_two_elements)
