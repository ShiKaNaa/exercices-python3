# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

for i in range(10):
    previous = i - 1
    sum_with_next = i + previous
    print(f'Current number is {i}, previous number is {previous}, sum is {sum_with_next}')
