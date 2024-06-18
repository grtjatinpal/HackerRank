
# n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    print(s)
    choice = input().split()
    # Use a match statement to perform operations based on the choice
    match choice[0].lower():
        case "remove":
            s.remove(int(choice[1]))
        case "pop":
            s.pop()
        case "discard":
            s.discard(int(choice[1]))
        case _:
            print("Enter correct input: Restart Program....")
            
print(sum(s))