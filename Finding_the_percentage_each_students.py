
n = int(input("Enter the number of students: "))
student_marks = {}  # Dictionary to store student names and their scores

# Loop to input student names and scores
for _ in range(n):
    name, *line = input("Enter student name followed by space-separated scores: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("Enter the name of the student to calculate average marks: ")

sum_score = 0

# Loop to calculate the sum of scores
for avg_marks in range(len(student_marks[query_name])):
    score = student_marks[query_name][avg_marks]
    sum_score = score + sum_score

    # If it's the last iteration, calculate and print the average
    if avg_marks == len(student_marks[query_name]) - 1:
        print(f"Average marks for {query_name}: {sum_score / len(student_marks[query_name]):.2f}%")
