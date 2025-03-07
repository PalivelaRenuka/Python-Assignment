'''string = "Hello"
print(string)
string1 = "Python"
print(string1)
string2 = """Welcome to the world of Python"""
print(string2)
print()


#2nd question
# Define two strings
string1 = "Hello, "
string2 = "python!"
# Concatenate the strings
result = string1 + string2
# Print the result
print(result)

#3rd question
my_string = "Python  is a programming language"
length = len(my_string)
print("The length of the string is:", length)

#4th question
my_string = "Hello, Python!"
substring = my_string[7:12]  
print(substring)

#5th question
text = "Hello, welcome to Python programming!"
position = text.index("Python")
print("The word 'Python' is found at index:", position)

#6th question
# List of strings
words = ["apple", "stawberry", "cherry"]
# Sort the list lexicographically
sorted_words = sorted(words)
print(sorted_words)

#7th question
str1 = "apple"
str2 = "banana"
if str1 == str2:
    print("Both strings are equal.")
elif str1 > str2:
    print(f'"{str1}" is greater than "{str2}".')
else:
    print(f'"{str1}" is smaller than "{str2}".')


#8th question












#9th question
my_string = "Hello, world!"
# Trim '*' characters
trimmed_string = my_string.strip('*')

print(f"Original string: '{my_string}'")
print(f"Trimmed string: '{trimmed_string}'")


#10th question
text = "I love Java"
new_text = text.replace("Java", "Python")
print("Replaced text:", new_text)


#11th
text = "apple,banana,grape"
words = text.split(",")
print("Split words:", words)

#12
num = int(input())
num_str = str(num)
print("Converted integer to string:", num_str)
print("Type of num_str:", type(num_str))
'''
#13
text = "Hello World"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
