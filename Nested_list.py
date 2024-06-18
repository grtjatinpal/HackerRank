def get_sorted_unique_scores(student_data):
    # Function to extract unique scores and sort them in ascending order
    scores = set()  # Use a set to store unique scores
    for marks in student_data.values():
        scores.add(marks)  # Add each score to the set
    sorted_scores = sorted(list(scores))  # Convert the set to a list and sort it
    return sorted_scores

def get_names_with_score(student_data, target_score):
    # Function to find names based on target score
    names = []
    for name, score in student_data.items():
        if target_score == score:
            names.append(name)  # Add names with the target score to the list
    sorted_names = sorted(names)  # Sort the list of names alphabetically
    return sorted_names

def display_names(names):
    # Function to display names
    for name in names:
        print(name)

if __name__ == '__main__':
    # Main program
    student_data = {}  # Dictionary to store student data
    for _ in range(int(input())):
        name = input()  # Input student name
        score = float(input())  # Input student score
        student_data[name] = score  # Add student data to dictionary
        
    # Get the second lowest score
    sorted_unique_scores = get_sorted_unique_scores(student_data)
    if len(sorted_unique_scores) > 1:
        second_lowest_score = sorted_unique_scores[1]
    else:
        second_lowest_score = sorted_unique_scores[0]
        
    # Find names with the second lowest score
    names_with_second_lowest_score = get_names_with_score(student_data, second_lowest_score)
    
    # Display the names
    display_names(names_with_second_lowest_score)
