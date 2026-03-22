# Day 2 - 30 Days of Python Challenge
# Variable

# Declare variables with various data types
first_name = 'Alex'
last_name = 'Guerrero'
full_name = 'Alex Guerrero'
country = 'US'
city = 'New York City'
age = 224
year = 2026
is_married = 'No'
is_true = 'Yes'
is_light_on = 'No'
multiple_variable = 'This year is 2026.'

# Printing out types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(multiple_variable))

print(len(first_name))
print(len(last_name))


num_one = 5
num_two = 4

variable_total = num_one + num_two
variable_diff = num_two - num_one
variable_product = num_one * num_two
variable_division = num_one / num_two
variable_remainder = num_two % num_one
variable_exp = num_one ** num_two
floor_division = num_one // num_two

print(variable_total)
print(variable_diff)
print(variable_product)
print(variable_division)
print(variable_remainder)
print(variable_exp)
print(floor_division)


radius = 30
area_of_circle = (radius ** 2) * 3.14
circum_of_circle = 2 * radius * 3.14

print(area_of_circle)
print(circum_of_circle)


user_input_radius = input('Insert radius: ')
user_input_area = ((float(user_input_radius) ** 2) * 3.14)

print(user_input_radius)
print(user_input_area)


user_first_name = input('Insert first name: ')
user_last_name = input('Insert last name: ')
user_country = input('Insert country: ')
user_age = input('Insert age: ')

print(user_first_name)
print(user_last_name)
print(user_country)
print(user_age)