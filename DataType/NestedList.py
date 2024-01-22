if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    unique_grades = sorted(set(score for name, score in records))
    second_lowest_grade = unique_grades[1]
    second_lowest_students = sorted([name for name, score in records if score == second_lowest_grade])
    for student in second_lowest_students:
        print(student)
