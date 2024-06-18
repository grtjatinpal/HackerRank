
Height, Width = map(int,input().split(" ") ) # Height, Width

Line = 1
Dot = Line * 2
Dash = (Width - (Dot + Line)) // 2
# Upper part of the door mat
for i in range(1, Height, 2):
    pattern = (".|." * i).center(Width, '-')
    print(pattern)

# Welcome message
print("WELCOME".center(Width, '-'))

# Lower part of the door mat
for i in range(Height-2, 0, -2):
    pattern = (".|." * i).center(Width, '-')
    print(pattern)
