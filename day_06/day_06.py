# Day 6 - 30 Days of Python Challenge

# Tuples

# Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()
print('1. Create an empty tuple: ', empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
names = ('Carlos', 'Mela', 'Mathew', 'Gigi')
print('2. Create a tuple containing names: ', names)

# 3. Join brothers and sisters tuples and assign it to siblings
brothers = ('Carlos', 'Matt')
sisters = ('Mela', 'Gigi')
siblings = brothers + sisters
print('3. Join brothers and sisters tuples and assign it to siblings: ', siblings)

# 4. How many siblings do you have?
print('4. How many siblings do you have?: ', len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Jorge', 'Maria')
print('5. Modify the siblings tuple and add the name of your father and mother: ', family_members)


# Exercises: Level 2

# 1. Unpack siblings and parents from family_members
*siblings_unpacked, father, mother = family_members
print('1a. Unpack siblings: ', siblings_unpacked)
print('1b. Unpack parents (father): ', father)
print('1c. Unpack parents (mother): ', mother)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrots', 'peppers', 'broccoli')
animal_products = ('milk', 'eggs', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
print('2. food_stuff_tp: ', food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('3. food_stuff_lt: ', food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print('4. Slice out the middle item: ', food_stuff_lt[len(food_stuff_lt) // 2])

# 5. Slice out the first three items and the last three items from food_stuff_lt list
print('5a. First three items: ', food_stuff_lt[:3])
print('5b. Last three items: ', food_stuff_lt[-3:])

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
print('6. Delete the food_stuff_tp tuple completely')
# print(food_stuff_tp)

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('7a. Check if Estonia is a nordic country: ', 'Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('7b. Check if Iceland is a nordic country: ', 'Iceland' in nordic_countries)