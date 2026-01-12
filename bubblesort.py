# Create a list of numbers to be sorted
numbers = [5,3,8,4,2]

# Find the total number of elements in the list
n = len(numbers)

# Outer loop controls the number of passes
# Runs (n-1) times because after each pass,the largest element moves to the end
for i in range(n - 1):

    # Inner loop compares adjacent elements
    # (n-1-i) avoids already sorted elements at the end
    for j in range(n - 1 - i):

        # Check if the current element is greater than the next element
        if numbers[j] > numbers[j+1]:

            # Swap the two elements if they are in the wrong order
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            
# Print the sorted list after all passes are complete
print("Sorted list:", numbers)
