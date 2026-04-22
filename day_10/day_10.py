# Day 10 - 30 Days of Python Challenge

# Loops

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
print('1a. Iterate 0 to 10 using for loop')
for number in range(11):
    print(number)
print()

print('1b. Iterate 0 to 10 using while loop')
count = 0
while count <= 10:
    print(count)
    count += 1
print()

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
print('2a. Iterate 10 to 0 using for loop')
for number in range(10, -1, -1):
    print(number)
print()


print('2b. Iterate 10 to 0 using while loop')
count = 10
while count >= 0:
    print(count)
    count -= 1
print()

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print('3. Write a loop that makes the following triangle: ')
for i in range(1,8):
    print('#' * i)
print()

# 4. Use nested loops to create the following:
print('4. Use nested loops to create the following: ')
for i in range(8):
    for j in range(8):
        print('#', end= ' ')
    print()

# 5. Print the following pattern:
print('5. Print the following pattern: ')
for i in range(11):
    print(f'{i} x {i} = {i*i}')
print()

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop")
for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(i)
print()

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
print('7. Use for loop to iterate from 0 to 100 and print only even numbers: ')
for i in range(0,101):
    if i % 2 == 0:
        print(i, end= ' ')
print()

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
print('8. Use for loop to iterate from 0 to 100 and print only odd numbers: ')
for i in range(0,101):
     if i % 2 != 0:
        print(i, end= ' ') 
print()


# Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print('1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.')
sum = 0
for i in range(0,101):
    sum += i
print(f'The sum of all numbers is {sum}')
print()

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print('2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds: ')
even_sum = 0
odd_sum = 0
for i in range(0,101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')
print()


# Exercises: Level 3
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

# from countries import countries
# from countries_data import countries_data


# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# land_countries = []
# for country in countries:
#     if 'land' in country.lower():
#         land_countries.append(country)
# print('Countries containing land: ', land_countries)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print('2. Reverse the order of fruit list using loop.')
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)
print()

# 3. Go to the data folder and use the countries_data.py file.
#   What are the total number of languages in the data
#   Find the ten most spoken languages from the data
#   Find the 10 most populated countries in the world

