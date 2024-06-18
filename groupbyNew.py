def groupBy(arr):
    output = {}  # Initialize an empty dictionary to store the counts
    for key in arr:  # Iterate over each element in the array
        output[key] = (
            output.get(key, 0) + 1
        )  # Increment the count for the current element
    return output  # Return the dictionary containing the counts


# Initialize an empty dictionary to store the counts
output = {}

# Input the array
arr = list(input("Enter the array elements separated by spaces: "))

# Call the groupBy function to count the occurrences of each element
output = groupBy(arr)
for (
    key,
    group_Size,
) in output.items():  # Iterate over the key-value pairs in the dictionary
    print(f"Count {key}: Group Size {group_Size}")
