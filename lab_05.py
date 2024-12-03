# Answer 1
point_one = tuple([int(x) for x in input().split()])
point_two = tuple([int(x) for x in input().split()])
distance = 0
for index in range(3):
    distance += (point_one[index] - point_two[index]) ** 2
print(distance**0.5)

# Answer 2
coord_one = tuple([int(x) for x in input("Enter x1 and y1: ").split()])
coord_two = tuple([int(x) for x in input("Enter x2 and y2: ").split()])

line_equation = f"(x-{coord_one[0]}) = {(coord_one[0]-coord_two[0])/(coord_one[1]-coord_two[1])}(y-{coord_one[1]})"
print(line_equation)

# Answer 3
input_sentence = input("Enter a sentence: ")
frequency_dict = {}
for char in input_sentence:
    frequency_dict[char] = frequency_dict.get(char, 0) + 1
print(frequency_dict)

# Answer 4
names_list = [x for x in input("Enter customer name: ").split()]
ids_list = [x for x in input("Enter customer id: ").split()]
points_list = [x for x in input("Enter shopping point: ").split()]
zipped_customers = list(zip(names_list, ids_list, points_list))
print(zipped_customers)
formatted_list = []
for index in range(min(len(ids_list), len(names_list), len(points_list))):
    tuple_entry = (names_list[index], ids_list[index], points_list[index])
    formatted_list.append(tuple_entry)

print(formatted_list)

# Answer 5
sorted_list = sorted(formatted_list, key=lambda x: x[1])
print(f"Sorted using sorted function {sorted_list}")

for outer in range(len(formatted_list)):
    for inner in range(outer + 1, len(formatted_list)):
        if formatted_list[outer][1] > formatted_list[inner][1]:
            formatted_list[outer], formatted_list[inner] = (
                formatted_list[inner],
                formatted_list[outer],
            )

print(f"Sorted using bubble sort {formatted_list}")
