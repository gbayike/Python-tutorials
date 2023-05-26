# Get the number of students' records.
n = int(input())

# Create a dictionary to store the students' marks.
marks = {}

# Read the students' names and marks.
for i in range(n):
    name, *marks_list = input().split()
    marks[name] = marks_list

# Get the name of the student to query.
student_name = input()

# Calculate the average of the marks for the student.
average = sum(marks[student_name]) / len(marks[student_name])

# Print the average.
print(average)