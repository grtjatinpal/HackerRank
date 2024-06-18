
# Iterate over the number of test cases
for i in range(int(input("Enter the number of loop run"))):
    # Input the number of elements in set A
    set_A_elements = int(input("Enter the number of elements in Set A"))
    
    # Input elements
    set_A = set(map(int, input().split()))
    
    # Input the number of elements in set B
    set_B_elements = int(input("Enter the number of elements in Set B"))
    
    # Input elements
    set_B = set(map(int, input().split()))
    
    
    # Check if set A is a subset of set B
    # A is a subset of B if every element of A is also an element of B
    if set_A.issubset(set_B): # Example: If set A = {1, 2} and set B = {1, 2, 3}, then A is a subset of B.
        print(True)  # Print True if set A is a subset of set B
    else:
        print(False)  # Print False if set A is not a subset of set B
        

    # Check if set A is a superset of set B
    if set_A.issuperset(set_B): # Example: If set A = {1, 2, 3} and set B = {1, 2}, then A is a superset of B
        print("Set A is a superset of set B")
    else:
        print("Set A is not a superset of set B")