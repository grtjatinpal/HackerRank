from collections import Counter

# Question -
#           The first line contains , the number of shoes.
#           The second line contains the space separated list of all the shoes sizes in the shop.
#           The third line contains , the number of customers.
#           The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.


# with get function
def self_counter1(arr):
    counts = {}
    for size in arr:
        counts[size] = counts.get(size, 0) + 1
    return counts


# With out get function
def self_counter2(arr):
    counts = {}
    for size in arr:
        if size in counts:
            counts[size] += 1
        else:
            counts[size] = 1
    return counts


shoes_shelf = dict()  # Create Empty Shelf

income = 0  # Initialize income to zero

# Input the total number of shoes
numOfShoes = int(input("Enter the Total Number Of Shoes: "))

# Input the sizes of shoes
SizeOF_shoes = list(map(int, input("Size of Shoes: ").split()))

# Count the occurrences of each shoe size and store it in the shelf dictionary
shoes_shelf = self_counter1(SizeOF_shoes)
# shoes_shelf = self_counter2(SizeOF_shoes)

# Input the number of customers and Process each customer
for num in range(int(input("Number Of Customer: "))):
    # Input the size and price of the shoe the customer wants to buy
    size, prize = map(
        int,
        input(f"Customer {num + 1}: Size, Prize (separated by space): ")
        .strip()
        .split(),
    )
    # Check if the requested size is available in the shelf
    if size in shoes_shelf and shoes_shelf[size] > 0:
        shoes_shelf[size] -= 1
        income += prize
    else:
        # If not available, inform the customer
        print(f"Size {size} no longer available, so no purchase")

# Print the total income
print(f"Total Income: {income}")
