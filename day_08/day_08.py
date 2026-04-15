# Day 8 - 30 Days of Python Challenge

# Dictionaries

# 1. Create an empty dictionary called dog
dog = {}
print('1. Create an empty dictionary called dog: ', dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['Name'] = 'Max'
dog['Color'] = 'Black'
dog['Breed'] = 'Pitbull'
dog['Legs'] = 4
dog['Age'] = 1
print('2. Dog dictionary: ', dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Zendeya',
    'last_name' : 'Holland',
    'gender' : 'Female',
    'age' : 28,
    'marital_status' : 'Married',
    'skills' : ['SQL', 'Python'],
    'country' : 'USA',
    'city' : 'Los Angeles',
    'address' : '123 Street'
}
print('3. Student dictionary: ', student)

# 4. Get the length of the student dictionary
print('4. Get the length of the student dictionary: ', len(student))

# 5. Get the value of skills and check the data type, it should be a list
print('5a. Get the value of skills: ', student['skills'])
print('5b. Skills data type: ', type(student['skills']))

# 6. Modify the skills values by adding one or two skills

# 7. Get the dictionary keys as a list

# 8. Get the dictionary values as a list

# 9. Change the dictionary to a list of tuples using items() method

# 10. Delete one of the items in the dictionary

# 11. Delete one of the dictionaries
