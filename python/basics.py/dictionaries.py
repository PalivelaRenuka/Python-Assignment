# 1. Create a Dictionary with at least 5 key-value pairs of the Student ID and Name
students = {1: 'renu', 2: 'anjani', 3: 'sri', 4: 'jsri', 5: 'shiva'}
print("Original Dictionary:", students)

# 1.1. Adding the values in the dictionary
students[6] = 'ram'
print("\nDictionary after adding a new student:", students)

# 1.2. Updating the values in the dictionary
students[3] = 'krish'  # Update the value for student ID 3
print("\nDictionary after updating a value:", students)

# 1.3. Accessing the value in the dictionary
print("\nAccessing the value of student ID 1:", students[1])

# 1.4. Create a nested dictionary
nested_dict = {1: 'renu', 2: 'anjani', 3: {'Age': 20, 'Branch': 'IT', 'Year': 'Second Year'}}
print("\nNested Dictionary:", nested_dict)

# 1.5. Accessing the values of the nested dictionary
print("\nAccessing nested dictionary for student ID 3:", nested_dict[3])

# 1.6. Print the keys present in a particular dictionary
print("\nKeys in the student dictionary:", students.keys())

# 1.7. Delete a value from the dictionary
del students[6]  # Delete student with ID 6
print("\nDictionary after deleting a student:", students)
