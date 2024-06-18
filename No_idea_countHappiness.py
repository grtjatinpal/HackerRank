# If the script is executed as the main program
if __name__ == "__main__":
    # Initialize happiness
    happiness = 0
    
    # Input: Size of array and set
    no_of_elements_main_set = int(input("Enter the Main elements Size"))
    no_of_elements_other_set = int(input("Enter the other elements Size"))

    
    # Input: Array of integers
    # The strip() function in Python is used to remove leading and trailing whitespace characters (spaces, tabs, newlines) from a string. 
    arr = list(map(int, input().strip().split(' ')))
    
    # Input: Set A containing 'good' integers
    good_happiness = set(map(int, input().strip().split(' ')))
    
    # Input: Set B containing 'bad' integers
    bad_happiness = set(map(int, input().strip().split(' ')))
    
    # Iterate over the array
    for i in arr:
        # If the integer is in set A, increase happiness
        if i in good_happiness:
            happiness += 1
        # If the integer is in set B, decrease happiness
        elif i in bad_happiness:
            happiness -= 1
    
    # Print the final happiness value
    print(happiness)
