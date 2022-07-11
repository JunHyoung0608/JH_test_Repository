def print_numbers(*args): #*args <- variable_argument
    for arg in args:
        print(arg)

print_numbers(10)
print_numbers(10, 20, 30, 40)