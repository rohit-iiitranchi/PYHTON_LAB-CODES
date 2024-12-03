# Answer 1
words_list = [x for x in input().split()]
palindrome_count = 0
for single_word in words_list:
    reversed_word = single_word[::-1]
    if single_word == reversed_word:
        palindrome_count = palindrome_count + 1

print(f"Number of palindromes : {palindrome_count}")

# Answer 2
num_list = [int(x) for x in input().split()]
mean_value, median_value, mode_value = 0, 0, 0
num_list.sort()
sum_of_numbers = sum(num_list)
mean_value = sum_of_numbers / len(num_list)
print(f"Mean : {mean_value}")

if len(num_list) % 2 == 0:
    median_value = (num_list[len(num_list) // 2] + num_list[len(num_list) // 2 - 1]) / 2
else:
    median_value = num_list[len(num_list) // 2]

print(f"Median : {median_value}")

highest_count = 0
for element in num_list:
    if num_list.count(element) > highest_count:
        highest_count = num_list.count(element)
        mode_value = element

print(f"Mode : {mode_value}")

# Answer 3
course_codes = ["CS2001", "MA2001", "CS2003", "EC2001", "EC2003"]
course_names = [
    "Python Programming",
    "Mathematics",
    "Computer Organisation and Architechure",
    "Analog and Linear IC",
    "Circuit Analysis and Synthesis",
]
zipped_list = list(zip(course_codes, course_names))
print(zipped_list)

# Answer 4
singer_set = {x for x in input("Enter Singers").split()}
dancer_set = {x for x in input("Enter Dancers").split()}
print(f"All Artists : {singer_set | dancer_set}")
print(f"Alrounders : {singer_set & dancer_set}")
print(f"Singers only : {singer_set - dancer_set}")
print(f"Dancers only : {dancer_set - singer_set}")
print(f"Dancers but not Singers cum Singers but not Dancers: {singer_set ^ dancer_set}")
