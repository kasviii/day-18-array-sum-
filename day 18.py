def find_subarray_with_sum(array, target_sum):
    current_sum = array[0]
    start_index = 0

    for i in range(1, len(array)):
        # Remove elements from the start of the subarray until the current sum is less than or equal to the target sum
        while current_sum > target_sum and start_index < i - 1:
            current_sum -= array[start_index]
            start_index += 1
        
        # If current sum equals target sum, return the subarray
        if current_sum == target_sum:
            return array[start_index:i]
        
        # Add the next element to the current sum
        current_sum += array[i]

    # Check for the last subarray
    if current_sum == target_sum:
        return array[start_index:]

    return None

# Input array from the user
array = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Target sum from the user
target_sum = int(input("Enter the target sum: "))

# Find and print the subarray with the target sum
result = find_subarray_with_sum(array, target_sum)
if result:
    print("Subarray with a sum of", target_sum, ":", result)
else:
    print("No subarray found with a sum of", target_sum)

