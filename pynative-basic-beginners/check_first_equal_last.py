# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False

def first_equal_last(array_of_int):
    return True if array_of_int[0] == array_of_int.last else False

first_equal_last([75, 65, 35, 75, 30])
first_equal_last([10, 20, 30, 40, 10])
