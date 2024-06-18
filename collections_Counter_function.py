from collections import Counter

# Initialize income to zero
income = 0

# Read the total number of shoes available
number_of_shoes = int(input("Enter the Number of shoes: "))

# Read the sizes of available shoes and count them using Counter
shoes_numbers = Counter(map(int, input("Enter All shoes Number: ").split()))

# Iterate over the number of customers
for i in range(int(input("Number of Customer"))):
    # Read the size and price of the shoe the customer wants to buy
    size, price = map(int, input("Shoes No. with Price: ").split())

    # Check if the requested size is available
    if shoes_numbers[size] > 0:
        # If available, update the income and decrease the quantity of available shoes in that size
        income += price
        shoes_numbers[size] -= 1

# Print the total income earned from selling shoes
print(income)
