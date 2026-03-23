# Day 3 - 30 Days of Python Challenge

# Operators

# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
age = 18
height = 5.1
complex_number = 1 + 1j

print(age)
print(height)
print(complex_number)


# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
user_base = input('Enter base: ')
user_height = input('Enter height: ')
area_of_triangle = 0.5 * user_base * user_height

print('The area of the triangle is ', area_of_triangle)


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
user_base_a = input('Enter side a: ')
user_base_b = input('Enter side b: ')
user_base_c = input('Enter side c: ')
perimeter_of_triangle = user_base_a + user_base_b + user_base_c

print('The perimeter of the triangle is ', perimeter_of_triangle)


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
user_length = input('Enter length: ')
user_width = input('Enter width: ')
rectangle_area = user_length * user_width
rectangle_perimeter = 2 * (user_length + user_width)

print('The area of rectangle is ', rectangle_area)
print('The perimeter of rectangle is ', rectangle_perimeter)


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
user_radius = input('Enter radius: ')
circle_area = 3.14 * user_radius ** 2
circle_circumference = 2 * 3.14 * user_radius

print('The area of circle is ', circle_area)
print('The circumference of circle is ', circle_circumference)


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2

print('The slope is ', slope)
print('The y-intercept is ', y_intercept)


# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope_2 = (10 - 2) / (6 - 2)
distance = (((2-6) ** 2) + ((2-10) ** 2)) ** (1/2)

print('The slope is ', slope_2)
print('The distance is ', distance)


# Compare the slopes in tasks 8 and 9.
print('The first slope is', slope, '. The second slope is', slope_2)
print('slope > slope_2: ', slope > slope_2)
print('slope < slope_2: ', slope < slope_2 )
print('slope == slope_2: ', slope == slope_2)


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
user_x = input('Insert a x value: ')
y = user_x ** 2 + 6 * user_x + 9

print('The value of y (y = x^2 + 6x + 9) is ', y)


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print('The length of python is ', len('python'))
print('The length of dragon is ', len('dragon'))
print(len('python') == len('dragon'))


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in python', 'on' in 'python')
print('on in dragon', 'on' in 'dragon')


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon in ')


# There is no 'on' in both dragon and python


# Find the length of the text python and convert the value to float and convert it to string


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.


# Check if type of '10' is equal to type of 10


# Check if int('9.8') is equal to 10


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years


# Write a Python script that displays the following table