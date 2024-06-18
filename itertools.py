from itertools import combinations

# Take input as a string and split it into a list of strings
string_S = list(map(str, input().strip().split()))

# Convert the second element of the list to an integer
string_S[1] = int(string_S[1])

# Initialize an empty list to store the combinations
result = []

# Generate combinations of characters from the input string
for size in range(string_S[1]):
    # Generate combinations of size 'size+1' (to include combinations of all sizes from 1 to 'string_S[1]')
    combinations_list = list(combinations(sorted(string_S[0].upper()), size+1))
    # Extend the 'result' list with the generated combinations
    result.extend(combinations_list)

# Iterate over the result list
for index, value in enumerate(result):
    # Convert each tuple of characters to a string
    result[index] = "".join(result[index])
    # Print each combination
    print(result[index])
