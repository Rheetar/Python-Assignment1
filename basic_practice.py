# TASK 1;
# Variables and Data Types:

# Declare variables
num1 = 10   # integer 
num2 = 3.14 # float
name = "Brian Smith"    # string

# Print values and types of variables
print("num1:", num1, "Type:", type(num1))
print("num2:", num2, "Type:", type(num2))
print("name:", name, "Type:", type(name))


# TASK 2;
# User Input

# Prompt user to enter their age
age = int(input("Enter your age: "))

# check user age and print message based on the age entered
if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# TASK 3;

# Conditional Statements

# Function to check number
def check_number(num):
    if num > 0:
        print("Positive number.")
    elif num < 0:
        print("Negative number.")
    else:
        print("Zero.")

# Test the function with different integer values
check_number(5)
check_number(-3)
check_number(0)


# TASK 4;
# Loops

# Print all even numbers from 0 to 20
print("Even numbers from 0 to 20:")
for i in range(0, 21, 2):
    print(i)


# TASK 5;
# Functions

# Function to calculate circle area
def calculate_circle_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

# Test the function with different values of redius 2 and 3
print("Area of circle with radius 2:", calculate_circle_area(2))
print("Area of circle with radius 3:", calculate_circle_area(3))