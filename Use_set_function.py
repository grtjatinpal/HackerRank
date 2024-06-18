# create with inbuilt function
# def Set_values(arr: set, value):
#     return arr.add(value)

# Set: Supports set-specific methods like add(), remove(), union(), intersection(), etc.
# List: Supports list-specific methods like append(), remove(), extend(), sort(), etc.
# Tuple: Being immutable, tuples have fewer methods compared to sets and lists. They support methods like count() and index().

arr = set({})
Number_of_country = int(input())
for i in range(Number_of_country):
    Country_name = input()
    
    # set is unorder list so this not use to append() function is use add() function
    arr.add(Country_name)
    
print(len(arr))