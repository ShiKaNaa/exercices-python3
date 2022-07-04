# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

previous = 0

for i in range(10):
    previous -= i
    next = i + 1
    print(f'Current number is {i}, previous number is {previous}, next is {next}')
