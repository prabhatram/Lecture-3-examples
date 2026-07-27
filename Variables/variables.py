# Python Variable Types

# 1. Integer - whole numbers
age = 25
count = -10
zero = 0

# 2. Float - decimal numbers
price = 19.99
temperature = -5.5
pi = 3.14159

# 3. Boolean - True or False
print(bool("Hello"))  # True: non-empty string
print(bool(2))        # True: non-zero number
print(bool(0))        # False: zero
print(bool(None))     # False: None
print(bool(""))       # False: empty string
print(bool([]))       # False: empty list
print(bool([1, 2]))   # True: non-empty list


# 4. String - text data
str1 = "Alice"
str2 = 'Alice'

# The following will cause a syntax error due to the single quote in the string
str3 = 'Alice's'    

# The following is the correct way to include a single quote in a string
str4 = "Alice's"

# Similarly, the following will cause a syntax error due to the double quote in the string
str5 = "Alice said, "Hello!""

# The following is the correct way to include double quotes in a string
str6 = 'Alice said, "Hello!"'

multiline = """This is a
multiline string"""

multiline_single = '''This is also a
multiline string'''


# 5. Character - single character strings
char1 = 'A' # This is a single character string. Meaning, a String of length 1. Python does not have a separate character type, so single characters are represented as strings of length 1.

str1 = "Hello"

first_char = str1[0]
print(first_char)  # H

last_char = str1[-1]
print(last_char)   # o

second_last_char = str1[-2]
print(second_last_char)  # l

name = "Alice"
name[0] = "B"  # This will raise a TypeError because strings are immutable in Python. Meaning, you cannot change a character in a string directly. You would need to create a new string if you want to modify it.
# Correct way to change the first character


# 5. Character and substring lookup
name = "Alice"

print("A" in name)  # True
print("B" in name)  # False
print("lice" in name)  # True
print("Bob" in name)  # False
print("alice" in name)  # False, Python is case-sensitive
print("cat" not in name)  # True, "cat" is not in "Alice"

# 5.1 Lookup using if-else 
name = "Alice"

if "A" in name:
    print("Found A in name")
else:
    print("A not found in name")

# 6 String concatenation
str1 = "James"
str2 = "Bond"
full_name = str1 + str2
print(full_name)  # Prints JamesBond  

full_name = str1 + " " + str2
print(full_name)  # Prints James Bond  

#7 Repeating a string
str1 = 'Candyman! '
repeated_str = str1 * 3
print(repeated_str)  # Prints Candyman! Candyman! Candyman!
print(str1 * 3)  # Also Prints Candyman! Candyman! Candyman!


#8. String length
str1 = "Aurora Borealis"
length = len(str1)
print(length)  # Prints 15, as the space is also counted as a character


#9. Slicing
str1 = "Aurora Borealis"
print(str1[0:3])  # Prints 'Aur', characters from index 0 to 2
print(str1[:3])   # Prints 'Aur', characters from the start to index 2, just like above
print(str1[7:])   # Prints 'Borealis', characters from index 7 to the end
print(str1[:4])   # Prints 'Auro', characters from the start to index 3
print(str1[-7:])  # Prints 'Borealis', last 7 characters
print(str1[:-8])  # Prints 'Aurora', all characters except the last 8

#10. Looping through a string
str1 = "Aurora Borealis"
for char in str1:
    print(char)  # Prints each character in the string on a new line


# 11. String formatting
name = "Sherlock Holmes"
age = 35
detail = name + " - " + age  # This will raise a TypeError because you cannot concatenate a string and an integer directly. You need to convert the integer to a string first.

#The following is the correct way to concatenate a string and an integer:
detail = name + " - " + str(age) 
print(detail)  # Prints Sherlock Holmes - 35

# 11.1 - f-string
print(f"{name} - {age}")    # Prints Sherlock Holmes - 35


# 11.2 - format method
print("{} - {}".format(name, age))  # Prints Sherlock Holmes - 35

# 11.3 - % formatting
print("%s - %d" % (name, age))  # Prints Sherlock Holmes - 35


# 12. String methods
str1 = "Hello world"
print(str1.upper())  # Prints "HELLO WORLD"
print(str1.lower())  # Prints "hello world"
print(str1.title())  # Prints "Hello World"

str2 = "  Apples, apples, apples, everywhere. "
print(str2.strip())  # Prints "Apples, apples, apples, everywhere." strip() removes leading and trailing whitespace
print(str2.replace("apples", "oranges"))  # Prints "  Apples, oranges, oranges, everywhere. "
print(str2.split(","))  # Prints ['  Apples', ' apples', ' apples', ' everywhere. '], splits the string into a list of substrings based on the delimiter ","
print(str2.count("apples"))  # Prints 2, counts the number of occurrences of the substring "apples". It's case-sensitive
print(str2.replace("apples", "oranges")) # Prints "  Apples, oranges, oranges, everywhere. ", replaces all occurrences of the substring "apples" with "oranges". It's case-sensitive
print(str2.count("apples", 4, 16))  # Counts the number of occurrences of the substring "apples" between index 0 and 15
print(str2.startswith("  Apples"))  # Prints True, checks if the string starts with the substring "  Apples". 
print(str2.endswith("everywhere. "))  # Prints True, checks if the string ends with the substring "everywhere. "
print(str2.find("apples"))  # Prints 10, returns the index of the first occurrence of the substring "apples". It's case-sensitive. Returns -1 if not found   
print(str2.isalpha())  # Prints False, checks if all characters in the string are alphabetic. Returns False because of spaces and punctuation
print(str2.isalnum())  # Prints False, checks if all characters in the string are alphanumeric. Returns False because of spaces and punctuation
str3 = "2 Apples."
print(str3.isalnum())  # Prints False, checks if all characters in the string are alphanumeric. Returns False because of spaces and punctuation
print(str3.isdigit())  # Prints False, checks if all characters in the string are digits. Returns False because of letters and punctuation

# Basic variable Type checking
age = 35              # int
height = 1.75         # float
name = "Alice"        # str
is_student = True     # bool
middle_name = None    # NoneType

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
print(type(middle_name))

# 5. List - ordered, mutable collection
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

# 6. Tuple - ordered, immutable collection
coordinates = (10, 20)
rgb = (255, 128, 0)
single_tuple = (42,)

# 7. Dictionary - key-value pairs
person = {"name": "Bob", "age": 30, "city": "New York"}
scores = {"math": 95, "english": 87, "science": 92}

# 8. Set - unordered, unique elements
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}

# 9. NoneType - represents absence of value
nothing = None
result = None

# 10. Complex - complex numbers
complex_num = 3 + 4j
z = complex(2, -5)

# Type checking
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(price))  # <class 'float'>
print(type(is_active))  # <class 'bool'>
print(type(fruits))  # <class 'list'>
print(type(coordinates))  # <class 'tuple'>
print(type(person))  # <class 'dict'>
print(type(unique_numbers))  # <class 'set'>
print(type(nothing))  # <class 'NoneType'>
print(type(complex_num))  # <class 'complex'>
