# Day 10 - 30 Days of Python Challenge

# Loops

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
print('1a. Iterate 0 to 10 using for loop')
for number in list(range(11)):
    print(number)

print('1b. Iterate 0 to 10 using while loop')
count = 0
while count <= 10:
    print(count)
    count += 1


# 2. Iterate 10 to 0 using for loop, do the same using while loop.
print('2a. Iterate 10 to 0 using for loop')
for number in list(range(11).reverse()):
    print(number)

print('2b. Iterate 10 to 0 using while loop')
count = 10
while count >= 0:
    print(count)
    count -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

# Use for loop to iterate from 0 to 100 and print only even numbers

# Use for loop to iterate from 0 to 100 and print only odd numbers


# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# The sum of all evens is 2550. And the sum of all odds is 2500.


# Exercises: Level 3

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world