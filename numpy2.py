import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)

print("First value:", numbers[0])

print("Last value:", numbers[-1])

print("First three values:", numbers[0:3])

students = np.array([
    [80, 90, 70],
    [60, 75, 85]
])

print("2D Array:")
print(students)

print("First row:", students[0])

print("First row, second value:", students[0, 1])

print("Shape:", students.shape)

print("Dimensions:", students.ndim)