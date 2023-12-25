
# Define the array
arr = [5, 10, 20, 30]

# Iterate through the array using a for loop
for i in range(len(arr) -1):
    # Calculate the sum of adjacent numbers
    total = arr[i] + arr[i + 1]
    
    # Print the sum
    print(total)