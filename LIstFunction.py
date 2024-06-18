My_list = []

# Loop for the number of commands
for i in range(int(input("Enter the number of commands: "))):
    
    # Get the choice from the user
    choice = input("Enter your choice (insert, print, remove, append, sort, pop, reverse): ").split(" ")
    

    # Convert numeric arguments to integers
    for _ in range(1, len(choice)):
        choice[_] = int(choice[_])

    # Use a match statement to perform operations based on the choice
    match choice[0].lower():
        case "insert":
            My_list.insert(choice[1], choice[2])
        case "print":
            print(My_list)
        case "remove":
            My_list.remove(choice[1])
        case "append":
            My_list.append(choice[1])
        case "sort":
            My_list.sort()
        case "pop":
            My_list.pop()
        case "reverse":
            My_list.reverse()
        case _:
            print("Enter correct input: Restart Program....")
