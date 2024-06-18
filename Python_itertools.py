# Import the permutations function from itertools module
from itertools import permutations

# Input the string and the number of characters to be selected
string, length = (
    input("Enter string and length seprated by space: ").upper().strip().split()
)

# Generate all permutations of the characters in the string with the specified length
output = list(permutations(string, int(length)))

# Iterate over each permutation, sorted in lexicographically increasing order
for char in sorted(output):
    # Print each permutation as a string
    print("".join(char))
