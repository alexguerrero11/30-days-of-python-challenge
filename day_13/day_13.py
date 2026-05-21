# Day 13 - 30 Days of Python Challenge

# List Comprehension

# Exercises: Level 1

# 1. Filter only negative and zero in the list using list comprehension
print('1. Filter only negative and zero in the list using list comprehension')

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero_number = [n for n in numbers if n <= 0]

print(negatives_and_zero_number)
print()

# 2.Flatten the following list of lists of lists to a one dimensional list :
print('2.Flatten the following list of lists of lists to a one dimensional list')

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [n for sub in list_of_lists for n in sub]

print(flatten_list)
print()
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 3. Using list comprehension create the following list of tuples:
print('3. Using list comprehension create the following list of tuples')

tuple_lst = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range (11)]

print(tuple_lst)
print()
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]


# 4. Flatten the following list to a new list:
print('4. Flatten the following list to a new list')

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries_list = [
    [country.upper(), country[:3].upper(), city.upper()]
    for subllist in countries
    for country, city in subllist
]

print(flatten_countries_list)
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# 5. Change the following list to a list of dictionaries:
print('5. Change the following list to a list of dictionaries')

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dictionaries = [
    {'country': country.upper(), 'city': city.upper()}
    for sublist in countries
    for country, city in sublist
]

print(country_dictionaries)
print()
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

# 6. Change the following list of lists to a list of concatenated strings:
print('6. Change the following list of lists to a list of concatenated strings')

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst_concatenated_strings = [
    first_name + ' ' + last_name
    for sublist in names
    for first_name, last_name in sublist
]

print(lst_concatenated_strings)
print()
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
print('7. Write a lambda function which can solve a slope or y-intercept of linear functions')

slope = lambda x1, y1, x2, y2: (y2-y1) / (x2-x1)
y_intercept = lambda x1, y1, x2, y2:  y1 - slope(x1, y1, x2, y2) * x1

print(f'Slope of (0,0) and (2,4): {slope(0, 0, 2, 4)}')
print(f'Y-intercept of (0,0) and (2,4): {y_intercept(0, 0, 2, 4)}')
print(f'Slope of (1,2) and (3,8):       {slope(1, 2, 3, 8)}')
print(f'Y-intercept of (1,2) and (3,8): {y_intercept(1, 2, 3, 8)}')