# Answer 1
def manipulate_string(input_string):
    print(input_string.swapcase())
    print(input_string[5:])
    print(input_string[5:] * 3)
    print("Mera", input_string[5:])
    print("Mera", input_string[5:], "Mahan")


string1 = "Maha Bharat"
manipulate_string(string1)


# Answer 2
def manipulate_string(string_data):
    print(len(string_data))
    print(string_data.find("e"))
    print(string_data.count("a"))
    print(string_data.replace("Ba", "Ta"))


string2 = "Ba Ba Black Sheep"
manipulate_string(string2)


# Answer 3
def check_palindrome(string_input):
    if string_input == string_input[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


string3 = input("Enter a string: ")
check_palindrome(string3)


# Answer 4
def student_details():
    student_name = input("Enter Name: ")
    roll_number = input("Enter Roll Number: ")
    student_marks = int(input("Enter Marks: "))
    if student_marks >= 90:
        grade_point = 10
        remark_message = "Outstanding"
    elif student_marks >= 80:
        grade_point = 9
        remark_message = "Very Good"
    elif student_marks >= 70:
        grade_point = 8
        remark_message = "Good"
    elif student_marks >= 60:
        grade_point = 7
        remark_message = "Average"
    elif student_marks >= 50:
        grade_point = 6
        remark_message = "Pass"
    else:
        grade_point = 0
        remark_message = "Fail"
    print("Name:", student_name)
    print("Roll Number:", roll_number)
    print("Marks:", student_marks)
    print("Grade Point:", grade_point)
    print("Remark:", remark_message)


student_details()


# Answer 5
def find_roots(coeff_a, coeff_b, coeff_c):
    discriminant = coeff_b**2 - 4 * coeff_a * coeff_c
    if discriminant > 0:
        root_one = (-coeff_b + discriminant**0.5) / (2 * coeff_a)
        root_two = (-coeff_b - discriminant**0.5) / (2 * coeff_a)
        print("Roots are:", root_one, root_two)
    elif discriminant == 0:
        root_single = -coeff_b / (2 * coeff_a)
        print("Both Roots are:", root_single)
    else:
        real_part = -coeff_b / (2 * coeff_a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * coeff_a)
        print(
            "Roots are:",
            real_part,
            "+",
            imaginary_part,
            "and",
            "i",
            real_part,
            "-",
            imaginary_part,
            "i",
        )


coeff_a = int(input("Enter a: "))
coeff_b = int(input("Enter b: "))
coeff_c = int(input("Enter c: "))
find_roots(coeff_a, coeff_b, coeff_c)
