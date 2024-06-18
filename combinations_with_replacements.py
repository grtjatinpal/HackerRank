from itertools import combinations_with_replacement

String, length = input("Enter the array elements separated by spaces: ").split()

result = combinations_with_replacement(sorted(String), int(length))
for combination in result:
    print("".join(combination))
