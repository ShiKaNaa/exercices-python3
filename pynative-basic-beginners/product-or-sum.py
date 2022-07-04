# https://pynative.com/python-basic-exercise-for-beginners/

def product_or_sum(first_number, second_number):
    if first_number * second_number >= 1000:
        sum = first_number + second_number
        print(sum)
    else:
        print(first_number * second_number)

product_or_sum(50,100)
product_or_sum(10,25)
