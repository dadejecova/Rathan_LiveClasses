
# ================================================================
#  PYTHON REFRESHER
#  8-Week Live Backend Developer Program
#  Instructor: Rathan Kumar
# ================================================================

# ------------------------------------------------
# 1. DATA TYPES
# ------------------------------------------------
# ✅ Python is dynamically typed (no need to declare types)
# ✅ Common types: int, float, str, bool
print (f"--- Data Types ---")
name = "Daniel"
age = 32
height = 1.83
is_active = True
print (f"Hello, {name}! and I'm {age} years old, my height is {height} meters and is and Active user: {is_active}")

# Type casting
# Converting a value from one data type to another
print (f"--- Type Casting ---")
age_str = "32"
age_int = int(age_str)  # Convert string to integer
print (f"Converted age: {age_int} (Type: {type(age_int)})")

# ------------------------------------------------
# 2. OPERATORS & EXPRESSIONS
# ------------------------------------------------
print (f"--- Operators & Expressions ---")
# ✅ Arithmetic: +, -, *, /, %, **
# Example comparisons
print (f"--- Arithmetic Operators ---")
x = 20
y = 10

sum = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponentiation = x ** 2
print (f"Sum: {sum}, Subtraction: {subtraction}, Multiplication: {multiplication}, Division: {division}, Modulus: {modulus}, Exponentiation: {exponentiation}")
# ✅ Comparison: ==, !=, >, <, >=, <=
print (f"--- Comparison Operators ---")
# Example comparisons
print (f"Equal: {x == y}, Not Equal: {x != y}, Greater: {x > y}, Less: {x < y}, Greater or Equal: {x >= y}, Less or Equal: {x <= y}")
# ✅ Logical: and, or, not
print (f"--- Logical Operators ---")
# Example comparisons
print (f"And x > 15 & y < 15: {x > 15 and y < 15}, Or x > 15 or y < 15: {x > 15 or y < 15}, Not X > 15: {not(x > 15)}")



# ------------------------------------------------
# 3. STRINGS & USER INPUT
# ------------------------------------------------
# ✅ Strings are immutable
# ✅ Use f-strings for formatting
print (f"--- Strings & User Input ---")

# Getting input
input_name = input("Enter your name: ")
input_age = input("Enter your age: ")
print (f"Hello, {input_name}! You are {input_age} years old.")


# ------------------------------------------------
# 4. COLLECTION DATA TYPES
# ------------------------------------------------
# ✅ List (mutable), Tuple (immutable), Set (unique), Dict (key-value)
print (f"--- Collection Data Types ---")
# List - mutable
print (f"--- List ---")

# Tuple - immutable
print (f"--- Tuple ---")


# Set - unique
print (f"--- Set ---")

# Dictionary - key-value pair
print (f"--- Dictionary ---")

# Loop through dictionary
print (f"--- Loop through Dictionary ---")


# ------------------------------------------------
# 5. CONDITIONS & LOOPS
# ------------------------------------------------
# ✅ if/elif/else for conditions
# ✅ for and while for iteration
print (f"--- Loops ---")

# For loop
print (f"--- For Loop ---")

# While loop
print (f"--- While Loop ---")


# ------------------------------------------------
# 6. LIST COMPREHENSIONS
# ------------------------------------------------
# ✅ Short way to create new lists using loops
# ✅ Common in Django when processing data
print (f"--- List Comprehensions ---")


# Filter example


# ------------------------------------------------
# 7. FUNCTIONS + LAMBDA + MAP/FILTER
# ------------------------------------------------
# ✅ Functions = reusable code blocks
# ✅ Lambda = short anonymous functions
# ✅ Map/Filter = apply or filter data from iterables
print (f"--- Functions ---")


# Lambda
# A lambda function is a small, anonymous function, meaning a function without a name



# ------------------------------------------------
# 8. FILE HANDLING
# ------------------------------------------------
# ✅ Use 'with open()' to handle files safely
# ✅ Modes: 'r' = read, 'w' = write, 'a' = append

print (f"--- File Handling ---")




# ------------------------------------------------
# 9. ERROR HANDLING
# ------------------------------------------------
# ✅ Use try/except to handle runtime errors gracefully
# ✅ Always handle specific exceptions






# ------------------------------------------------
# 10. MODULES & PACKAGES
# ------------------------------------------------
# ✅ Use built-in modules like math, os, random
# ✅ You can also create custom modules









