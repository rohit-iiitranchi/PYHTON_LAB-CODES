# Answer 1
import numpy as np
import matplotlib.pyplot as plt

case_data = np.array(
    [
        [1500, 2000, 1800, 1200, 900],  # Day 1
        [1600, 2100, 1900, 1300, 950],  # Day 2
        [1700, 2200, 2000, 1400, 1000],  # Day 3
        [1650, 2150, 1950, 1350, 980],  # Day 4
        [1750, 2250, 2050, 1450, 1020],  # Day 5
        [1800, 2300, 2100, 1500, 1050],  # Day 6
        [1900, 2400, 2200, 1600, 1100],  # Day 7
    ]
)

total_cases = case_data.sum(axis=0)
country_names = ["Nation_A", "Nation_B", "Nation_C", "Nation_D", "Nation_E"]
print("Total cases:")
for index in range(5):
    print(country_names[index], ":", total_cases[index])

max_country_index = np.where(total_cases == max(total_cases))
print("Country with max cases:", country_names[max_country_index[0][0]])


# Answer 2
average_daily_cases = case_data.sum(axis=0) // 7
print("Average daily cases:")
for index in range(5):
    print(country_names[index], ":", average_daily_cases[index])


# Answer 3
print("Daily Total Cases:")
daily_cases = case_data.sum(axis=1)
for day_index in range(7):
    print("Day", day_index + 1, ":", daily_cases[day_index])

max_day_index = np.where(daily_cases == max(daily_cases))
print("Day with max cases:", max_day_index[0][0] + 1)


# Answer 4
first_day_cases = case_data[0]
last_day_cases = case_data[-1]

percentage_changes = ((last_day_cases - first_day_cases) / first_day_cases * 100).round(
    1
)

nations = ["Nation_1", "Nation_2", "Nation_3", "Nation_4", "Nation_5"]
change_dict = dict(zip(nations, percentage_changes))

highest_increase_country = max(change_dict.items(), key=lambda x: x[1])

print("Percentage changes from Day 1 to Day 7:")
for nation, change in change_dict.items():
    print(f"{nation}: {change:+.1f}%")

print(
    f"\nCountry with highest increase: {highest_increase_country[0]} ({highest_increase_country[1]:+.1f}%)"
)


# Answer 5
def normalize_columns(data_matrix):
    normalized_matrix = np.zeros_like(data_matrix, dtype=float)
    for column_index in range(data_matrix.shape[1]):
        column_values = data_matrix[:, column_index]
        min_value = column_values.min()
        max_value = column_values.max()
        normalized_matrix[:, column_index] = (column_values - min_value) / (
            max_value - min_value
        )
    return normalized_matrix


normalized_case_data = normalize_columns(case_data)
normalized_case_data = np.round(normalized_case_data, 3)

print("Normalized COVID-19 data:")
print(normalized_case_data)


# Answer 6
time_days = np.arange(1, 8)
countries = ["Nation_A", "Nation_B", "Nation_C", "Nation_D", "Nation_E"]

daily_totals = case_data.sum(axis=1)
peak_day = time_days[np.argmax(daily_totals)]
peak_total_cases = np.max(daily_totals)

plt.figure(figsize=(12, 6))

line_colors = ["blue", "red", "green", "purple", "orange"]
for country_index in range(5):
    plt.plot(
        time_days,
        case_data[:, country_index],
        marker="o",
        label=countries[country_index],
        color=line_colors[country_index],
    )

plt.axvline(x=peak_day, color="gray", linestyle="--", alpha=0.5)
plt.annotate(
    f"Peak Day\nTotal: {peak_total_cases:,} cases",
    xy=(peak_day, peak_total_cases / 5),
    xytext=(peak_day + 0.3, peak_total_cases / 4),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

plt.title("Daily COVID-19 Cases by Nation", pad=20)
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(time_days)

plt.tight_layout()
plt.show()
