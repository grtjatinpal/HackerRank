#     123456789.|.987654321   21 - (2 - 1)//2 = 9
#     123456.|..|..|.123456
#     123.|..|..|..|..|.123
#     1234567WELCOME1234567
#     123.|..|..|..|..|.123
#     123456.|..|..|.123456
#     123456789.|.123456789


H = int(input("Enter the height of the door mat: "))
B = int(input("Enter the width of the door mat: "))  # width 3 times of height
Line = 1
Dot = Line * 2
Dash = (B - (Dot + Line)) // 2
# Upper part of the door mat
for i in range(1, H, 2):
    print("_" * Dash, ".|." * i, "_" * Dash)
    if Dash != 0:
        Line = Dash
        Dash = Dash - 3

# Welcome message
# print("_"*H,"WELCOME","_"*H)

Dash = Line
# Dash = (B - (Dot + Line)) // 2 # 21 - (2 - 1)//2 = 9
for i in range(H - 2, 0, -2):
    print("_" * Dash, ".|." * i, "_" * Dash)
    Dash = Dash + 3
