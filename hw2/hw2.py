# 2.3
grade = int(input("What is your grade? >"))

if grade >= 90:
    print(f"Congratulations! Your grade of {grade} earns you an A in this course!")

# 2.4
add = 27.2 + 2
sub = 27.5 - 2
times = 27.5 * 2
divide = 27.5 / 2
floor = 27.5 // 2
expo = 27.5 ** 2
print(f"Addition: {add}\nSubtraction: {sub}\nMultiplication: {times}\nDivision: {divide}\nFloor Division: {floor}\nExponent: {expo}")


# 2.5
radius = 2
n = 3.14159

print(f"Diameter: {2*radius}\nCircumference: {2*n*radius}\nArea: {n*radius**2}")


# 2.6
num = int(input("Please enter an integer >"))

if num % 2 == 0:
    print("You chose an even number!")
else:
    print("You chose an odd number")


# 2.7
num = 1024
num_2 = 2

if num % 4 == 0:
    print(f"{num} is a multiple of 4!")
else:
    print(f"{num} is not a multiple of 4")

if num_2 % 10 == 