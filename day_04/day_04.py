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
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28. Does 'Coding For All' start with a substring Coding?
# 29. Does 'Coding For All' end with a substring coding?