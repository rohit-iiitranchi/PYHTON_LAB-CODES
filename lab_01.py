# Answer 1
import math
import cmath

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum: ", num1 + num2)
print("Difference: ", num1 - num2)
print("Product: ", num1 * num2)
print("Integer quotient: ", num1 // num2)
print("Remainder: ", num1 % num2)
print("Fractional quotient: ", num1 / num2)

# Answer 2
side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))
semi_perimeter = (side1 + side2 + side3) / 2
triangle_area = math.sqrt(
    semi_perimeter
    * (semi_perimeter - side1)
    * (semi_perimeter - side2)
    * (semi_perimeter - side3)
)
triangle_perimeter = side1 + side2 + side3
print("Area of the triangle: ", triangle_area)
print("Perimeter of the triangle: ", triangle_perimeter)

angle1 = math.degrees(math.acos((side2**2 + side3**2 - side1**2) / (2 * side2 * side3)))
angle2 = math.degrees(math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3)))
angle3 = math.degrees(math.acos((side1**2 + side2**2 - side3**2) / (2 * side1 * side2)))
print("Angle 1: ", angle1)
print("Angle 2: ", angle2)
print("Angle 3: ", angle3)

# Answer 3
impedance1 = complex(input("Enter the first impedance: "))
impedance2 = complex(input("Enter the second impedance: "))
equivalent_impedance = 1 / ((1 / impedance1) + (1 / impedance2))
print("Z1: ", impedance1)
print("Z2: ", impedance2)
print("Real part of the equivalent impedance: ", equivalent_impedance.real)
print("Imaginary part of the equivalent impedance: ", equivalent_impedance.imag)
