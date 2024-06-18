number = 17

# Determine the width of the formatted strings
# format function mai b binary ko represent krta h 
white_space = len("{:b}".format(number))

# Loop to print the formatted strings for each number
for i in range(1, number + 1):
    decimal = i
    octal = oct(i)[2:]
    hexadecimal = hex(i)[2:].upper()
    binary = bin(i)[2:]

    # Print the formatted row
    # index = 0, width = " ", d = decimal, o = octal, b = binary
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(decimal, octal, hexadecimal, binary, width=white_space))