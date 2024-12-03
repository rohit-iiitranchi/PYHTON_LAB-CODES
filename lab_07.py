# Answer 1
import matplotlib.pyplot as plt

# Madhya Pradesh
party_labels = ["BJP", "INC", "BSP", "Others"]
mp_seat_counts = [163, 66, 0, 1]
mp_explode = (0.1, 0, 0, 0)
mp_fig, mp_ax = plt.subplots()
mp_ax.pie(
    mp_seat_counts,
    explode=mp_explode,
    labels=party_labels,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)
mp_ax.axis("equal")
plt.title("Madhya Pradesh")
plt.show()

# Rajasthan
rj_seat_counts = [69, 115, 2, 13]
rj_explode = (0, 0.1, 0, 0)
rj_fig, rj_ax = plt.subplots()
rj_ax.pie(
    rj_seat_counts,
    explode=rj_explode,
    labels=party_labels,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)
rj_ax.axis("equal")
plt.title("Rajasthan")
plt.show()

# Bar Chart
state_labels = ["BJP", "INC", "BSP", "Others"]
mp_values = [163, 66, 0, 1]
rj_values = [115, 69, 2, 13]
x_indices = range(len(state_labels))
bar_fig, bar_ax = plt.subplots()
bar_ax.bar(x_indices, mp_values, width=0.4, label="Madhya Pradesh", align="center")
bar_ax.bar(x_indices, rj_values, width=0.4, label="Rajasthan", align="edge")
plt.xticks(x_indices, state_labels)
plt.legend()
plt.title("Madhya Pradesh vs Rajasthan")
plt.show()

# Answer 2
num_values = int(input("Enter the number of values (min. 10): "))
max_value = int(
    input("Enter the maximum value till where numbers are to be generated: ")
)
import random

random_numbers = []
if num_values < 10:
    print("Please enter a number greater than 10")
    exit()
for _ in range(num_values):
    random_numbers.append(random.randint(1, max_value))
print(random_numbers)


def identify_primes():
    primes_list = []
    composites_list = []
    for number in random_numbers:
        if number > 1:
            for divisor in range(2, number):
                if number % divisor == 0:
                    composites_list.append(number)
                    break
            else:
                primes_list.append(number)
    return primes_list, composites_list


def calculate_squares(primes_list):
    squared_primes = []
    for prime in primes_list:
        squared_primes.append(prime**2)
    return squared_primes


def calculate_square_roots(composites_list):
    square_roots = []
    for composite in composites_list:
        square_roots.append(composite**0.5)
    return square_roots


primes_list, composites_list = identify_primes()

squared_primes = calculate_squares(primes_list)
square_roots_composites = calculate_square_roots(composites_list)

import matplotlib.pyplot as plt
import numpy as np

prime_numbers_array = np.array(primes_list)
squared_primes_array = np.array(squared_primes)

plt.subplot(1, 2, 1)
plt.scatter(prime_numbers_array, squared_primes_array)
plt.xlabel("Prime Numbers")
plt.ylabel("Square of Prime Numbers")
plt.title("Prime Numbers vs Square")

composite_numbers_array = np.array(composites_list)
square_roots_array = np.array(square_roots_composites)
plt.subplot(1, 2, 2)
plt.scatter(composite_numbers_array, square_roots_array)
plt.xlabel("Composite Numbers")
plt.ylabel("Square root of Composite Numbers")
plt.title("Composite Numbers vs Square root")

# Set the spacing between subplots
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.show()
