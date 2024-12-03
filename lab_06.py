# Answer 1
def custom_zip(names_list, ids_list, points_list, strict_flag):
    if strict_flag == True:
        if len(names_list) == len(ids_list) == len(points_list):
            return list(zip(names_list, ids_list, points_list))
        else:
            return "Length of the lists are not equal"
    else:
        return list(zip(names_list, ids_list, points_list))


names_list = [x for x in input("Enter customer name: ").split()]
ids_list = [int(x) for x in input("Enter customer id: ").split()]
points_list = [int(x) for x in input("Enter shopping point: ").split()]
strict_flag = bool(input("Enter True or False: "))
result_list = custom_zip(names_list, ids_list, points_list, strict_flag)

print(result_list)


# Answer 2
def custom_sort(result_list, sort_key):
    if sort_key == 0:
        result_list.sort(key=lambda x: x[0])
    elif sort_key == 1:
        result_list.sort(key=lambda x: x[1])
    elif sort_key == 2:
        result_list.sort(key=lambda x: x[2])


sort_key = int(input("Enter the key: "))
sorted_result_list = custom_sort(result_list, sort_key)
print(result_list)


# ANSWER 3
def custom_max(input_args):
    max_value = 0
    for item in input_args:
        if item > max_value:
            max_value = item
    return max_value


input_set = {int(x) for x in input("Enter the numbers: ").split()}
maximum_number = custom_max(input_set)
print(maximum_number)

# ANSWER 4
input_string = input("Enter the string: ")


def custom_upper(input_string):
    return input_string.upper()


uppercase_string = custom_upper(input_string)
print(uppercase_string)


def square_digits(input_string):
    digit_list = [int(x) for x in input_string.split() if x.isdigit()]
    return [x**2 for x in digit_list]


squared_list = square_digits(input_string)
print(squared_list)


def find_alphanumerics(input_string):
    return [x for x in input_string.split() if x.isalnum()]


alphanumeric_list = find_alphanumerics(input_string)
print(alphanumeric_list)
