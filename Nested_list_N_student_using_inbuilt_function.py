
# Create a dictionary to store student names and grades
Store_student_data_dic = {}

for _ in range(int(input("Number of Student: "))): # "Number of Students: "
    name = input("Enter the student name: ").capitalize() # "Student Name: "
    score = float(input(f"{name} Score: ")) # "Student Marks: "
    # Name is key in Dictionary
    Store_student_data_dic[name] = score

print(Store_student_data_dic)
    
# values() aapko dictonary values ka ek list deta hai
grades = sorted(set(Store_student_data_dic.values())) # Find the second lowest grade

  # Check if there are at least two distinct grades
if len(grades) > 1:
#    New Variable = set_name[index]
    second_lowest_grade = grades[1]
else:
    second_lowest_grade = grades[0]
    

second_lowest_students = []

# List comprehension ka istemaal karke students ke names ko extract karein jinke grades second lowest hain
second_lowest_students = [name for name, grade in Store_student_data_dic.items() if grade == second_lowest_grade]

# sort names    
second_lowest_students = sorted(second_lowest_students)

# items() ka use seh hum key and ushke items ko dono ka use kr sakte hain
# Find students using second lowest grade
for name in second_lowest_students:
    print(name)