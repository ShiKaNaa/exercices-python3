# 1
# 2 2
# 3 3 3
# 4 4 4 4

def print_n_times(number_to_print):
    for num in range(number_to_print):
        for i in range(num):
            print(num, end=" ")
        print("\n")

num = int(input("Please enter a number: "))
print(print_n_times(num))
