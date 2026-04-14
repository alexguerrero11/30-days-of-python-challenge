# Day 7 - 30 Days of Python Challenge

# Sets

# Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print('1. Find the length of the set it_companies', len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('2. Add Twitter to it_companies: ', it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta', 'X'])
print('3. Insert multiple IT companies at once to the set it_companies: ', it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print('4. Remove one of the companies from the set it_companies: ', it_companies)

# 5. What is the difference between remove and discard
print('5a. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set.')
print('5b. However, discard() method does not raise any errors.')


# Exercises: Level 2

# 1. Join A and B
print('1. Join A and B: ', A.union(B))

# 2. Find A intersection B
print('2. Find A intersection B: ', A.intersection(B))

# 3. Is A subset of B
print('3. Is A subset of B: ', A.issubset(B))

# 4. Are A and B disjoint sets
print('4. Are A and B disjoint sets: ', A.isdisjoint(B))

# 5. Join A with B and B with A
print('5a. Join A with B: ', A.union(B))
print('5b. Join B with A: ', B.union(A))

# 6. What is the symmetric difference between A and B
print('6. What is the symmetric difference between A and B: ', A.symmetric_difference(B))

# 7. Delete the sets completely
print('7a. Delete the sets completely', A.clear())
print('7b. Delete the sets completely', B.clear())


# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
print('Age list: ', age)
print('Age set: ', ages)
print('Length of the list: ', len(age))
print('Length of the set: ', len(ages))
print('List is bigger as set removes duplicates.')

# 2. Explain the difference between the following data types: string, list, tuple and set
print('''
Data Type Differences:
---------------------------------------------------------
String  - Ordered, immutable, stores characters only.
          Supports indexing and slicing.
          Example: name = "Python"

List    - Ordered, mutable, allows duplicates.
          Can store mixed data types.
          Example: items = [1, "hello", 3.14]

Tuple   - Ordered, immutable, allows duplicates.
          Faster than lists; used for fixed collections.
          Example: coords = (10, 20)

Set     - Unordered, mutable, NO duplicates allowed.
          Great for membership tests and set operations.
          Example: unique = {1, 2, 3}
---------------------------------------------------------
''')

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
word_set = set(words)

print('Sentence: ', sentence)
print('All words: ', words)
print('Unique words: ', word_set)
print('Number of unique words: ', len(word_set))