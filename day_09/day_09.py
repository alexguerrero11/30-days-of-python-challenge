# Day 9 - 30 Days of Python Challenge

# Conditionals

# Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.
user_age = int(input('Enter age: '))

if user_age >= 18:
    print('You are old enough to drive.')
else:
    remaining_years = 18 - user_age
    print(f'You need {remaining_years} years to learn to drive.')

# 2. Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 20
your_age = int(input('Enter age: '))
age_difference = your_age - my_age

if my_age == your_age:
    print('We are the same age.')
elif my_age > your_age:
    if( my_age - your_age) == 1:
        print(f'I am 1 year older than you.')
    else:
        print(f'I am {my_age - your_age} years older than you.')
elif your_age > my_age:
    if( your_age - my_age) == 1:
        print(f'You are 1 year older than me.')
    else:
        print(f'You are {your_age - my_age} years older than me.')


# 3. Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, 
# else a is equal to b. Output:
number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: '))

if number_one > number_two:
    print(f'{number_one} is greater than {number_two}')
else:
    print(f'{number_one} is smaller than {number_two}')


# Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
student_grade = int(input('Enter score for letter grade: '))

if student_grade >= 90:
    print('Letter Grade: A')
elif student_grade >= 80:
    print('Letter Grade: B')
elif student_grade >= 70:
    print('Letter Grade: C')
elif student_grade >= 60:
    print('Letter Grade: D')
else: 
    print('Letter Grade: F')

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
input_month = input('Enter month: ').capitalize()

if input_month in ['September', 'October', 'November']:
    print('Season: Autumn')
elif input_month in ['December', 'January', 'February']:
    print('Season: Winter')
elif input_month in ['March', 'April', 'May']:
    print('Season: Spring')
if input_month in ['June', 'July', 'August']:
    print('Season: Summer')


# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
input_fruit = input('Enter a fruit: ').lower()

if input_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(input_fruit)
    print('Updated fruit list: ', fruits)


# Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 20,
    'country': 'US',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check for skills key, then print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"Middle skill: {skills[middle_index]}")

# Check if Python is in the skills list
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python: {has_python}")

# Determine title based on skill set
skills = person.get('skills', [])
skills_set = set(skills)

if skills_set == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
    print('He is a fullstack developer')
else:
    print('unknown title')

#  If the person is married and if he lives in US, print the information in the following format:
#     Asabeneh Yetayeh lives in US. He is married.
if person['is_married'] == True and person['country'] == 'US':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')