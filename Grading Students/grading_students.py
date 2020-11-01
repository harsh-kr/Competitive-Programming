def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] > 37:
            if (grades[i] % 5) != 0:
                if 5 - (grades[i] % 5) < 3:
                    grades[i] += 5 - (grades[i] % 5)
    return grades


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)