n = int(input())
grade = []

for _ in range(n):
    input_data = input().split()
    grade.append((input_data[0], int(input_data[1])))


grade = sorted(grade, key=lambda student: student[1])

for student in grade:
    print(student[0], end=' ')
