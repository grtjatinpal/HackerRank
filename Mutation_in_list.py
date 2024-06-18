input_string = "abracadabra     "

# string convert to list
string_list = list(input_string)

# get position and character from user input
position, character = input("Enter position and character separated by space: example-> 5 k ").split()

# change character using position
string_list[int(position)] = character
print(string_list)
