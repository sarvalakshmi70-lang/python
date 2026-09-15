def calculate_total(marks):
    total = sum(marks)
    return total


def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


name = "Sarva"
age = 20
course = "Python"

marks = [80, 75, 90, 85, 95]

subjects = ("Python", "Java", "SQL", "Maths", "English")

student = {
    "name": name,
    "age": age,
    "course": course
}

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

print("\nSubjects:")

for subject in subjects:
    print(subject)

print("\nMarks:")

for mark in marks:
    print(mark)

total = calculate_total(marks)
average = calculate_average(marks)

print("\nTotal Marks:", total)
print("Average Marks:", average)

squares = [mark * mark for mark in marks]

print("\nSquare of Each Mark:")
print(squares)

print("\nFirst Three Marks:")
print(marks[:3])

print("\nLast Two Marks:")
print(marks[-2:])

print("\nMathematical Operations:")

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

