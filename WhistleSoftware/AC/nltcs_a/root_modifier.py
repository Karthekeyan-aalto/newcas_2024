import re

# Read the file contents
with open('nltcs_equation.txt', 'r') as file:
    equation = file.read()

# Define a function to calculate the 5th root of a number
def fifth_root(match):
    number = float(match.group())
    return f'{number ** (1/5):.6f}'

# Use regular expression to find all numbers that are between 0 and 1
modified_equation = re.sub(r'0\.\d+', fifth_root, equation)

# Write the modified equation to a new file
with open('modified_equation.txt', 'w') as file:
    file.write(modified_equation)

modified_equation
