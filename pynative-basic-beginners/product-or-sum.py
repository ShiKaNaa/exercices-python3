# https://pynative.com/python-basic-exercise-for-beginners/

first_input = int(input("Donnez un premier chiffre: "))
second_input = int(input("Donnez un second chiffre: "))

def product_or_sum(first_number, second_number):
    if first_number * second_number >= 1000:
        sum = first_number + second_number
        print(sum)
    else:
        print(first_number * second_number)

product_or_sum(first_input, second_input)
