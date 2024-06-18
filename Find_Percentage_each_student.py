if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    student_avg = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        student_avg[name] = sum(scores)/len(scores)
    query_name = input()
    print(f"{student_avg[query_name]:.2f}")
    