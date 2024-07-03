# This is a comment. Comments are ignored by the Python interpreter.
# Comments are used to explain the code and make it more readable.

# Print a message to the console
print("Hello, World!")  # The print() function outputs text to the console.

# Variables and Data Types
a = 10  # Integer (int)
b = 3.14  # Floating point number (float)
c = "Python"  # String (str)
d = True  # Boolean (bool)

# Print the values and types of the variables
print("a =", a, "type:", type(a))
print("b =", b, "type:", type(b))
print("c =", c, "type:", type(c))
print("d =", d, "type:", type(d))

# Basic Arithmetic Operations
sum_result = a + b  # Addition
diff_result = a - b  # Subtraction
prod_result = a * b  # Multiplication
quot_result = a / b  # Division

# Print the results of the arithmetic operations
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Quotient:", quot_result)

# Conditional Statements
if a > b:
    print("a is greater than b")  # This block executes if the condition is True
else:
    print("a is not greater than b")  # This block executes if the condition is False

# Loops
# For loop to iterate over a range of numbers
for i in range(5):  # range(5) generates numbers from 0 to 4
    print("i =", i)

# While loop to iterate until a condition is met
count = 0
while count < 5:
    print("count =", count)
    count += 1  # Increment count by 1

# Functions
def greet(name):
    """
    This is a function named greet.
    It takes one parameter 'name' and prints a greeting message.
    """
    print("Hello, " + name + "!")

# Call the greet function
greet("Alice")
greet("Bob")

# Lists
fruits = ["apple", "banana", "cherry"]  # A list of fruits
print("Fruits:", fruits)

# Append an item to the list
fruits.append("date")
print("Updated Fruits:", fruits)

# Loop through the list and print each item
for fruit in fruits:
    print("Fruit:", fruit)

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}  # A dictionary representing a person

# Print the dictionary
print("Person:", person)

# Access dictionary items
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Add a new key-value pair to the dictionary
person["job"] = "Engineer"
print("Updated Person:", person)

# Function with Return Value
def add(x, y):
    """
    This function takes two parameters 'x' and 'y'.
    It returns their sum.
    """
    return x + y

# Call the add function and print the result
result = add(5, 7)
print("Sum of 5 and 7 is:", result)
