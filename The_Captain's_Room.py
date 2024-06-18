# Ye code slower hai
# solution 1
def Captain_Room1(Room_List: list):
    Room_Set = set(Room_List)
    # Unique room numbers nikal ne k liye and set mai indexing nhi hoti toh list m convert kya
    for Room_number in list(Room_Set):
        # Check karta hai agar room number sirf ek baar list mein hai
        if Room_List.count(Room_number) == 1:
            return Room_number

# Solution 2
def Captain_Room2(Room_List: list):
    Room_Set = set(Room_List)
    # Room numbers ko list se remove karta hai
    for Room_number in Room_Set:
        Room_List.remove(Room_number)

    # Captain ka room number dhundta hai
    Room_number = Room_Set.difference(set(Room_List))
    return Room_number.pop() #pop() function use Convert set to int

# Solution 3
def Captain_Room3(Room_List: list):
    room_count = {}
    
    # for room_number in Room_List:
    #     room_count[room_number] = room_count.get(room_number, 0) + 1

    for room_number in Room_List:
        room_count.setdefault(room_number, 0)
        # room_count[room_number] += 1
        room_count[room_number] = room_count[room_number] + 1 # increment in value
    
    print(f"Room Count:- {room_count}")  # Debug print
    
    for room_number, count in room_count.items():
        if count == 1:
            return room_number


# main <==========================--------------==========================> main

# Input: Groups ka count
No_of_group = int(input())

# Input: Har group ke liye allowed room capacities ki list
Room_List = list(map(int, input().split()))

# Room numbers set se find kiye jaate hain
Room_Set = set(Room_List)

# Agar milta hai, toh room number print kiya jaata hai
# print(Captain_Room1(Room_List))
# print(Captain_Room2(Room_List))
print(Captain_Room3(Room_List))
