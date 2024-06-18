# The first line contains an integer, N, the number of students.
# The 2N  subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

def find_second_lowest_students(record):
    # 'inf' Python mein infinity (anant) ko represent karne ke liye ek special floating-point value hai.
    lowest_grade = float('inf')
    second_lowest_grade = float('inf')
    count = 0

    # Find second lowest student
    for student_score in record:
        score = student_score[1]

        # Agar yeh grade current lowest grade se kam hai
        if score < lowest_grade:
            second_lowest_grade = lowest_grade
            count = 1
            lowest_grade = score

        # Agar yeh grade doosre lowest grade ke barabar hai
        elif second_lowest_grade == score:
            count += 1
            
        # Agar yeh second_lowest kam hain
        # elif(score > lowest_grade and score < second_lowest_grade):
        elif lowest_grade < score < second_lowest_grade:
            second_lowest_grade = score

    second_lowest_students = []
    # second lowest grade wale students ka name and Grade list mein daalein
    for student_score in record:
        if student_score[1] == second_lowest_grade:
            second_lowest_students.append(student_score[0])

    return second_lowest_students

def sort_words(List):
    # Selection sort ka use karke list ko sort karein
    for i in range(len(List)):
        for j in range(1, len(List)):
            if List[j - 1] > List[j]: # yeah sidha word k saath mach kr sakte h 
                List[j - 1], List[j] = List[j], List[j - 1]

    return List

record = []
for _ in range(int(input("Number of Students: "))):
    name = input("Student Name: ")
    score = float(input("Student Marks: "))
    record.append([name, score])

# Doosre lowest grade wale students ko dhundhein
second_lowest_students = find_second_lowest_students(record)

# Students ke naam ko aksharik kram mein sort karein
sorted_second_lowest_students = sort_words(second_lowest_students)

# Result ko print karein
print("Second Lowest Grade Students:")
for student in sorted_second_lowest_students:
    print(student)
