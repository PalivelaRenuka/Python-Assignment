# 1. Add integer values of an array
def sum_array(arr):
    return sum(arr)

# 2. Calculate the average value of an array
def average_array(arr):
    return sum(arr) / len(arr)

# 3. Find the index of an array element
def find_index(arr, element):
    return arr.index(element) if element in arr else -1

# 4. Test if array contains a specific value
def contains(arr, value):
    return value in arr

# 5. Remove a specific element from an array
def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

# 6. Copy an array to another array
def copy_array(arr):
    return arr.copy()

# 7. Insert an element at a specific position in the array
def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr

# 8. Find the minimum and maximum value of an array
def min_max(arr):
    return min(arr), max(arr)

# 9. Reverse an array of integer values
def reverse_array(arr):
    return arr[::-1]

# 10. Find the duplicate values of an array
def find_duplicates(arr):
    seen = set()
    duplicates = []
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# 11. Find the common values between two arrays
def common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

# 12. Remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))

# 13. Find the second largest number in an array
def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()
    return arr[-2] if len(arr) > 1 else None

# 14. Find the second largest number in an array (same as task 13)
# (Same code as task 13)

# 15. Count the number of even and odd numbers in an array
def count_even_odd(arr):
    even = sum(1 for x in arr if x % 2 == 0)
    odd = len(arr) - even
    return even, odd

# 16. Get the difference of the largest and smallest value
def difference(arr):
    return max(arr) - min(arr)

# 17. Verify if the array contains two specified elements (12, 23)
def contains_elements(arr, a, b):
    return a in arr and b in arr

# 18. Remove duplicate elements and return the new array
def remove_duplicates(arr):
    return list(set(arr))

# Example arrays to test the functions

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 2, 3, 4, 4]

# Testing the functions
print(sum_array(arr1))  # Output: 15
print(average_array(arr1))  # Output: 3.0
print(find_index(arr1, 3))  # Output: 2
print(contains(arr1, 3))  # Output: True
print(remove_element(arr1, 3))  # Output: [1, 2, 4, 5]
print(copy_array(arr1))  # Output: [1, 2, 3, 4, 5]
print(insert_element(arr1, 2, 10))  # Output: [1, 2, 10, 3, 4, 5]
print(min_max(arr1))  # Output: (1, 5)
print(reverse_array(arr1))  # Output: [5, 4, 3, 2, 1]
print(find_duplicates(arr2))  # Output: [2, 4]
print(common_values(arr1, arr2))  # Output: [1, 2, 3, 4]
print(remove_duplicates(arr2))  # Output: [1, 2, 3, 4]
print(second_largest(arr1))  # Output: 4
print(count_even_odd(arr1))  # Output: (2, 3)
print(difference(arr1))  # Output: 4
print(contains_elements(arr1, 2, 3))  # Output: True
print(remove_duplicates(arr2))  # Output: [1, 2, 3, 4]
