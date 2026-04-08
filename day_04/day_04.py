# Day 4 - 30 Days of Python Challenge

# Strings
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word1 = 'Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = 'Python'
string1 = f'{word1} {word2} {word3} {word4}'
print("Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string: ",string1)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word5 = 'Coding'
word6 = 'For'
word7 = 'All'
string2 = f'{word5} {word6} {word7}'
print("Concatenate the string 'Coding', 'For' , 'All' to a single string: ", string2)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print('Print the variable company and initial value: ', company)

# 5. Print the length of the company string using len() method and print().
print("Print the length of the company string: ", len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print('Change all the characters to uppercase letters: ', company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print('Change all the characters to lowercase letters: ', company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('Print capitalize: ', company.capitalize())
print('Print Title: ', company.title())
print('Print swapcase: ', company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print('Cut(slice) out the first word: ', company[:company.index(' ')])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Check if string contains a word Coding using index: ', company.index('Coding'))
print('Check if string contains a word Coding using find: ', company.find('Coding'))
print('Check if string contains a word Coding using in: ', 'Coding' in company)

# 11. Replace the word coding in the string 'Coding For All' to Python.
print('Replace the word coding in the string Coding For All to Python: ', company.replace('Coding', 'Python'))

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print('Change "Python for Everyone" to "Python for All" using the replace method: ', "Python for Everyone".replace('Everyone', 'All'))

# 13. Split the string 'Coding For All' using space as the separator (split())
print('Split the string Coding For All using space as the separator: ', company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon split the string at the comma: ', companies.split(', '))

# 15. What is the character at index 0 in the string Coding For All.
print('Character at index 0 in the string Coding For All: ', companies[0])

# 16. What is the last index of the string Coding For All.
print('Last index of the string Coding For All: ', len(companies) - 1)

# 17. What character is at index 10 in "Coding For All" string.
print('Character at index 10 in "Coding For All" string: ', company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
pfe = 'Python For Everyone'
print('Acronym or an abbreviation for the name Python For Everyone: ', ''.join([word[0] for word in pfe.split()]))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print('Acronym or an abbreviation for the name Coding For All: ', ''.join([word[0] for word in company.split()]))

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print('Determine the position of the first occurrence of C in Coding For All: ', company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print('Determine the position of the first occurrence of F in Coding For All: ', company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Determine the position of the last occurrence of l in Coding For All People: ', 'Coding For All People'.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print('Find the position of the first occurrence of the word because in the following sentence: ', sentence.index('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('Find the position of the last occurrence of the word because in the following sentence: ', sentence.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.index('because')
print('Slice out the phrase because because because in the following sentence: ', sentence[start_index:start_index + len('because because because')])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('Find the position of the first occurrence of the word because in the following sentence: ', sentence.find('because'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_index2 = sentence.find('because')
print('Slice out the phrase because because because in the following sentence: ', sentence[start_index2:start_index2 + len('because because because')])

# 28. Does 'Coding For All' start with a substring Coding?
print('Does Coding For All start with a substring Coding: ', company.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring coding?
print('Does Coding For All end with a substring Coding: ', company.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('Remove the left and right trailing spaces in the given string: ', '   Coding For All      '.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python
print('Which one of the following variables return True when we use the method isidentifier(): ')
print('30DaysOfPython: ', '30DaysOfPython'.isidentifier())
print('thirty_days_of_python: ', 'thirty_days_of_python'.isidentifier())

# 31. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('Join the list with a hash with space string: ', ' # '.join(libraries))

# 32. Use the new line escape sequence to separate the following sentences.
print('Use the new line escape sequence to separate the following sentences: ')
print('I am enjoying this challenge.\nI just wonder what is next.')

# 33. Use a tab escape sequence to write the following lines.
print('Use a tab escape sequence to write the following lines: ')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 34. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with radius {} is {:.2f} meters square.'.format(radius, area)
print(formated_string)

# 35. Make the following using string formatting methods:
a = 8
b = 6 
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')