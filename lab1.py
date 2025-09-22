# 1. Write a function to check if a number is positive, negative, or zero. Test the function with
# a few numbers.


def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


check_number(10)
check_number(-5)
check_number(0)

# 2. Create a function that takes a name as a parameter and returns a greeting. If no name is
# provided, it should default to "User".


def greet(name="User"):
    return f"Hello, {name}!"


print(greet())
print(greet("Alice"))

# 3. Write a function that takes a string and returns every second character from the string
# starting from index 1.


def every_second_char(s):
    return s[1::2]


print(every_second_char("Hello, World!"))
print(every_second_char("Python"))

# 4. Write a program that asks the user to input a number and then prints the number added
# to 5.

num = int(input("Enter a number: "))
result = num + 5
print(f"The result is: {result}")

# 5. Write a program that assigns a value to a variable, deletes it, and then tries to print it.
# Handle the error gracefully.

x = 10
del x
try:
    print(x)
except NameError:
    print("Variable 'x' is not defined.")

# 6. Create a function that checks if a number is even, odd, or zero, and prints the
# appropriate message. Test the function with different values.


def check_even_odd_zero(num):
    if num == 0:
        print("The number is zero.")
    elif num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


check_even_odd_zero(10)
check_even_odd_zero(7)
check_even_odd_zero(0)

# 7. Write a function that takes two numbers and returns their product. Test the function
# with different inputs.


def multiply(a, b):
    return a * b


print(multiply(5, 3))
print(multiply(10, 2))
print(multiply(-1, 8))

# 8. Create a function that takes a list of numbers and returns a new list containing the last
# three elements.


def last_three(lst):
    return lst[-3:]


print(last_three([1, 2, 3, 4, 5]))
print(last_three([6, 7, 8, 9, 10, 11]))

# 9. Write a program that takes a float input from the user and prints its double as an integer.

user_input = float(input("Enter a float number: "))
doubled_value = int(user_input * 2)
print(f"The double of {user_input} as an integer is: {doubled_value}")

# 10. Write a program that checks two variables and deletes one based on a condition. Print
# the remaining variable.

a = 15
b = 20
condition = a > b

if condition:
    del a
    print(b)
else:
    del b
    print(a)
