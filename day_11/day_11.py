# Day 11 - 30 Days of Python Challenge

# Functions

# Exercises: Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print('1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.')

def add_two_numbers(a, b):
    return a + b

print('Sum of two numners (6, 2): ', add_two_numbers(6, 2))
print()


# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
print('2. Write a function that calculates area_of_circle.')

import math

def area_of_circle(r):
    return math.pi * r * r

print('Area of circle (2 radius): ', area_of_circle(2))
print()


# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
print('3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments')

def add_all_nums(*args):
    for i in args:
        if not isinstance(i, (int, float)):
            return f'Error {i} is not a number.'
    return sum(args)
    
print('add_all_nums(1, 2, 3, 4):', add_all_nums(1, 2, 3, 4))
print('add_all_nums(1, 2, "a"):', add_all_nums(1, 2, 'a'))
print()


# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
print('4. Write a function which converts °C to °F.')

def convert_celsius_to_fahrenheit(C):
    return (C * 9 / 5) + 32

print('Temperature in °F (0 C): ', convert_celsius_to_fahrenheit(0))
print()


# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
print('5. Write a function called check-season, it takes a month parameter and returns the season.')

def check_season(month):
    month = month.strip().capitalize()

    if month in ['September', 'October', 'November']:
        return 'Season: Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Season: Winter'
    elif month in ['March', 'April', 'May']:
        return 'Season: Spring'
    elif month in ['June', 'July', 'August']:
        return 'Season: Summer'
    else:
        return 'Month not valid'

print('check_season("September"):', check_season('September'))
print('check_season("December"):', check_season('December'))
print('check_season("March"):', check_season('March'))
print('check_season("June"):', check_season('June'))
print()


# 6. Write a function called calculate_slope which return the slope of a linear equation
print('6. Write a function called calculate_slope which return the slope of a linear equation.')

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'Underfined (vertical line)'
    return (y2 - y1) / (x2 - x1)

print(f'Slope for (1, 1) and (4, 2): {calculate_slope(1, 1, 4, 2)}')
print()


# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print('7. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.')

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return(x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return 'No real solutions'

print('Solution for ax² + bx + c = 0: ', solve_quadratic_eqn(1, 2, 1))
print()


# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print('8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.')

def print_list(list):
    for i in list:
        print(i)

print('print_list([1, 2, 3]): ')
print_list([1, 2, 3])
print()


# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print('9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).')

def reverse_list(lst):
    reverse_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reverse_lst.append(lst[i])
    return reverse_lst

print('reverse_list([1, 2, 3, 4, 5]):', reverse_list([1, 2, 3, 4, 5]))
print('reverse_list(["A", "B", "C"]):', reverse_list(['A', 'B', 'C']))
print()


# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
print('10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items')

def capitalize_list_items(list):
    capitalized_list = []
    for i in list:
        capitalized_list.append(i.capitalize())
    return capitalized_list

print('capitalize_list_items(["i", "love", "python"]):', capitalize_list_items(['i', 'love', 'python']))
print()


# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
print('11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.')

def add_item(lst, item):
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))
print()


# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
print('12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.')

def remove_item(lst, item):
    lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
print()


# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print('13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.')

def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
print()


# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print('# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.')

def sum_of_odds(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 != 0:
            sum += i
    return sum

print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))
print()


# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
print('# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.')

def sum_of_even(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_of_even(5))
print(sum_of_even(10))
print(sum_of_even(100))
print()


## Exercises: Level 2


# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
print('# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.')

def evens_and_odds(num):
    odds = 0
    even = 0
    for i in range(num + 1):
        if i % 2 != 0:
            odds += 1
        else:
            even += 1
    print(f'The number of odds are {odds}.')
    print(f'The number of evens are {even}.')

print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.
print()


# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
print('2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number')

def factorial(num):
    if num == 0:
        return 1
    if num < 0:
        return 'Factorial is not defined for negative numbers'
    
    total = 1
    for i in range(1, num + 1):
        total *= i

    return total

print('factorial(0):', factorial(0))
print('factorial(5):', factorial(5))
print()


# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
print('3. Call your function is_empty, it takes a parameter and it checks if it is empty or not.')

def is_empty(par):
    return len(par) == 0

print('is_empty(""):', is_empty(''))
print('is_empty([1, 2]):', is_empty([1, 2]))
print()


# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print('# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).')

print()

# 5. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
print('5. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.')

def greet(name='Guest'):
    print(f'Hello, {name}!')

greet()
# "Hello, Guest!
greet("Alice")
# "Hello, Alice!"
print()

# 6. Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
print('6. Create a function called show_args to take an arbitrary number of named arguments and print their names and values.')
def show_args(**kwargs):
    parts = [f'{k}: {v}' for k, v in kwargs.items()]
    print('Received:', ', '.join(parts))


show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
print()