# Answer 1
number = int(input("Enter the number: "))
counter = 1
while counter <= number:
    print(counter, ":", counter * counter)
    counter += 1

# Answer 2
number_input = int(input("Enter the number: "))
original_number = number_input
digit_sum = 0
while number_input > 0:
    digit = number_input % 10
    digit_sum += digit
    number_input = number_input // 10
print("Sum of digits of", original_number, "is: ", digit_sum)

# Answer 3
fibonacci_count = int(input("Enter the number: "))
fib_a = 0
fib_b = 1
iteration = 0
while iteration < fibonacci_count:
    iteration += 1
    print(fib_a)
    fib_c = fib_a + fib_b
    fib_a = fib_b
    fib_b = fib_c

# Answer 4
multiplication_number = int(input("Enter the number: "))
multiplication_limit = int(input("Enter the limit: "))
multiplier = 1
while multiplier <= multiplication_limit:
    print(
        multiplication_number, "*", multiplier, "=", multiplication_number * multiplier
    )
    multiplier += 1

# Answer 5
string_input = input("Enter the string: ")
if string_input.isalnum():
    print("True, The string is alphanumeric")
else:
    print("False, The string is not alphanumeric")

# Answer 6
input_string = input("Enter the string: ")
character_to_count = input("Enter the character to be counted: ")
character_count = 0
for char in input_string:
    if char == character_to_count:
        character_count += 1
print(character_to_count, "is present", character_count, "times in", input_string)
