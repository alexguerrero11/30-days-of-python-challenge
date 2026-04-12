# Day 5 - 30 Days of Python Challenge

# Lists


# 1. Declare an empty list
empty_list = []
print('1. Declare an empty list: ', empty_list)

# 2. Declare a list with more than 5 items
list = ["computer", "mouse", "server", "monitor", "keyboard"]
print('2. Declare a list with more than 5 items: ', list)

# 3. Find the length of your list
print('3. Find the length of list: ', len(list))

# 4. Get the first item, the middle item and the last item of the list
print('4a. Get the first item from list: ', list[0])
print('4b. Get the middle item from list: ', list[len(list) // 2])
print('4c. Get the last item from list: ', list[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Yoda", 5, 2.2, "Single", "New York City"]
print('5. Declare a list called mixed_data_types: ', mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print('6. Declare a list variable named it_companies: ', it_companies)

# 7. Print the list using print()
print('7. Print the list: ', it_companies)

# 8. Print the number of companies in the list
print('8. Number of companies in the list: ', len(it_companies))

# 9. Print the first, middle and last company
print('9a. Print the first company: ', it_companies[0])
print('9b. Print the middle company: ', it_companies[len(it_companies) // 2])
print('9c. Print the last company: ', it_companies[len(it_companies) - 1])

# 10. Print the list after modifying one of the companies
it_companies[0] = "Meta"
print('10. List after modifying one of the companies: ', it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Nividia')
print('11. Add an IT company to it_companies: ', it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'X')
print('12. Insert an IT company in the middle of the companies list: ', it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[it_companies.index('Meta')] = 'Meta'.upper()
print('13. Change one of the it_companies names to uppercase (IBM excluded!): ', it_companies)

# 14. Join the it_companies with a string '#;  '
print('14. Join the it_companies with a string #; :', '#; '.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print('15. Check if a certain company exists in the it_companies list Apple: ', 'Apple' in it_companies)

# 16. Sort the list using sort() method
print('16. Sort the list using sort() method: ', it_companies.sort())

# 17. Reverse the list in descending order using reverse() method
print('17. Reverse the list in descending order using reverse() method: ', it_companies.reverse())

# 18. Slice out the first 3 companies from the list
print('18. Slice out the first 3 companies from the list: ', it_companies[3:])

# 19. Slice out the last 3 companies from the list
print('19. Slice out the last 3 companies from the list: ', it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
print('20. Slice out the middle IT company or companies from the list: ', it_companies[len(it_companies) // 2])

# 21. Remove the first IT company from the list
it_companies.remove(it_companies[0])
print('21. Remove the first IT company from the list: ', it_companies)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)
print('22. Remove the middle IT company or companies from the list: ', it_companies)

# 23. Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print('23. Remove the last IT company from the list: ', it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print('24. Remove all IT companies from the list: ', it_companies)

# 25. Destroy the IT companies list
del it_companies
print('25. IT companies list destroyed')
# print('Destroy the IT companies list: ', it_companies)

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
combined = front_end + back_end
print('26. Join the following lists: ', combined)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = combined.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')
print('27. Full stack: ', full_stack)

## Exercise: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print('Ages sorted: ', ages)
print('Min age: ', min(ages))
print('Max age: ', max(ages))

# Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))

print('Add the min age and the max age: ', ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median = ages[n // 2]
print('Median age:', median)

# Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print('Find the average age: ', round(average, 2))

# Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print('Find the range of the ages: ', age_range)

# Compare the value of (min - average) and (max - average), use abs() method
print('abs(min - average): ', abs(min(ages) - average))
print('abs(max - average): ', abs(max(ages) - average))

# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = country_list
print('\nChina:', china)
print('Russia:', russia)
print('USA:', usa)
print('Scandic countries:', scandic_countries)