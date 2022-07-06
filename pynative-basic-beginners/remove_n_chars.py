# Write a program to remove characters from a string starting from zero up to n and return a new string.
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.

def remove_chars(string_to_change, how_much):
    return string_to_change[how_much:]

string_to_change = input("please wright a word: ")
how_much = int(input("how much do you want to remove from the start: "))

print(remove_chars(string_to_change, how_much))
