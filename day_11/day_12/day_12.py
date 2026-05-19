# Day 12 - 30 Days of Python Challenge

# Modules

# Exercises: Level 1


# 1. Write a function which generates a six digit/character random_user_id.
print('1. Write a function which generates a six digit/character random_user_id.')
import string
import random

def random_user_id():
  lst = string.ascii_letters + string.digits
  return ''.join(random.choices(lst, k=6))

print(random_user_id())
print()

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print('2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.')

def user_id_gen_by_user():
  char_count = int(input('Enter number of characters: '))
  num_of_IDs = int(input('Enter number of IDs: '))
  lst = string.ascii_letters + string.digits

  for i in range(num_of_IDs):
    print(''.join(random.choices(lst, k=char_count)))

user_id_gen_by_user()
print()

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print('3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).')

def rgb_color_gen():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return f'rgb({r},{g},{b})'

print(rgb_color_gen())
print()


# Exercises: Level 2


# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
print('1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).')

def list_of_hexa_colors(n):
  color = []
  for i in range(n):
    color.append('#' + ''.join(random.choices(string.hexdigits[:16], k=6)))
  return color

print('Generate 2 hexadecimal colors: ', list_of_hexa_colors(2))
print()


# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print('2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.')

def list_of_rgb_colors(n):
  color = []
  for i in range(n):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color.append(f'rgb({r},{g},{b})')
  return color

print('Generate 2 RGB colors: ', list_of_rgb_colors(2))
print()

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(type, n):
  colors = []
  if type == 'hexa':
    colors.append(list_of_hexa_colors(n))
  if type == 'rgb':
    colors.append(list_of_rgb_colors(n))
  print(colors)

generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
print()


# Exercises: Level 3


# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print('1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list')

def shuffle_list(lst):
  copy_list = lst.copy()
  random.shuffle(copy_list)
  return copy_list

print('shuffle_list([1,2,3,4,5]):', shuffle_list([1, 2, 3, 4, 5]))
print()

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print('2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.')

def unique_random_number_list():
  return random.sample(range(9), 7)

print('Unique random number list:', unique_random_number_list())