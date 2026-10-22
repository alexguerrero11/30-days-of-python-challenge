# Day 14 - 30 Days of Python Challenge

# Higher Order Functions

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# 1. Explain the difference between map, filter, and reduce.
explaination = """
The map() function is a built-in function that takes a function and iterable as parameters.
The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.
The reduce() function calls
"""
print('1. Explain the difference between map, filter, and reduce.')
print(explaination)



# 2. Explain the difference between higher order function, closure and decorator
explaination2 = """

"""

print('# 2. Explain the difference between higher order function, closure and decorator.')

print()

# 3. Define a call function before map, filter or reduce, see examples.


# 4. Use for loop to print each country in the countries list.
print('4. Use for loop to print each country in the countries list.')
for country in countries:
    print(country)
print()

# 5. Use for to print each name in the names list.
print('5. Use for to print each name in the names list.')
for name in names:
    print(name)
print()

# 6. Use for to print each number in the numbers list.
print('# 6. Use for to print each number in the numbers list.')
for number in numbers:
    print(number)
print()


# Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase in the countries list
print('# 1. Use map to create a new list by changing each country to uppercase in the countries list')

def uppercase(word):
    return word.upper()

countries_upper_cased = map(uppercase, countries)
print(list(countries_upper_cased))
print()

# 2. Use map to create a new list by changing each number to its square in the numbers list
print('2. Use map to create a new list by changing each number to its square in the numbers list')

def square(num):
    return num ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared))
print()

# 3. Use map to change each name to uppercase in the names list
print('3. Use map to change each name to uppercase in the names list')

names_upper_case = map(uppercase, names)
print(list(names_upper_case))
print()


# 4. Use filter to filter out countries containing 'land'.
print('4. Use filter to filter out countries containing land')

def has_land(word):
    if 'land' not in word:
        return True
    return False

countries_without_land = filter(has_land, countries)
print(list(countries_without_land))
print()

# 5. Use filter to filter out countries having exactly six characters.
print('5. Use filter to filter out countries having exactly six characters.')

def has_six_characters(word):
    if len(word) == 6:
        return True
    return False

countries_with_six_characters = filter(has_six_characters, countries)
print(list(countries_with_six_characters))
print()

# 6. Use filter to filter out countries containing six letters and more in the country list.
print('6. Use filter to filter out countries containing six letters and more in the country list.')

def has_more_than_six_characters(word):
    if len(word) >= 6:
        return True
    return False

countries_with_more_than_six_characters = filter(has_more_than_six_characters, countries)
print(list(countries_with_more_than_six_characters))
print()

# 7. Use filter to filter out countries starting with an 'E'
print('7. Use filter to filter out countries starting with an E')

def starts_with_e(word):
    if word[0] == 'E':
        return True
    return False

countries_starting_with_e = filter(starts_with_e, countries)
print(list(countries_starting_with_e))
print()

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print('8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))')



# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
print('9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.')

def get_string_lists(list):
    for i in list:
        if type(i) == 'string':
            return True
        return False

names1 = filter(get_string_lists, names)
print(list(names1))
print()

# 10. Use reduce to sum all the numbers in the numbers list.
# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.