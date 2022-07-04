# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

accumulator = 0

for i in range(10):
    print(f'Current number is {i}, prévious number is {i-1}, total is {accumulator + i}')
