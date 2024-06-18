# Input: Size of array and set
no_of_elements_main_set = int(input("Enter the Main elements Size"))
no_of_elements_other_set = int(input("Enter the other elements Size"))

Happiness = {} # create Happiness dictionary 

# Input: Main set
main_set = list(map(int, input().split()))

# Input: Other set
other_set1 = list(map(int, input().split()))
other_set2 = list(map(int, input().split()))

# check each elements of the main set
for i in main_set:
    
    Happiness.setdefault("Current happiness", 0) # default Value dictionary
    # If the element is in Set A
    if i in other_set1:
        Happiness["Current happiness"] += 1 # increase happiness
    # If the element is in Set B
    elif i in other_set2:
        Happiness["Current happiness"] -= 1 # decrease happiness
    else:
        print("Happiness not found")
        
print(Happiness["Current happiness"])