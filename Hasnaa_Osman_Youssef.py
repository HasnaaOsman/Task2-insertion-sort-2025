# Problem:
# Given a sorted array in ascending order, insert a new number into the array 
# while maintaining the sorted order. 
# We cannot use sort() after inserting; instead, we must find the correct position 
# and insert the element directly.

# Example:
# Input array: [1, 3, 5, 7, 9]
# New number: 6
# Expected output: [1, 3, 5, 6, 7, 9]

def insert_sorted(arr, num):
    # Find the correct position for insertion
    for i in range(len(arr)):
        if arr[i] > num:
            arr.insert(i, num)  # Insert the number at the correct position
            return arr
    
    # If the number is greater than all elements, append it to the end
    arr.append(num)
    return arr

# Testing the function with the first dataset
arr = [1, 3, 5, 7, 9]
num = 6
print(insert_sorted(arr, num))  # Output: [1, 3, 5, 6, 7, 9]


# Applying the same logic to a different dataset:
# Input array: [2, 4, 8, 10]
# New number: 5
# Expected output: [2, 4, 5, 8, 10]

arr2 = [2, 4, 8, 10]
num2 = 5
print(insert_sorted(arr2, num2))  # Output: [2, 4, 5, 8, 10]