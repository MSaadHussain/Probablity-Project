import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

file_path = 'mean_data.xlsx'
data = pd.read_excel(file_path)

class_intervals = data['Class Interval']
frequencies = data['Frequency']

midpoints = []
for interval in class_intervals:
    lower, upper = map(float, interval.split('-'))
    midpoints.append((lower + upper) / 2)

midpoints = np.array(midpoints)
frequencies = np.array(frequencies)

mean = np.average(midpoints, weights=frequencies)

cum_freq = np.cumsum(frequencies)
total_freq = cum_freq[-1]

median_class_index = np.where(cum_freq >= total_freq / 2)[0][0]
median_class = class_intervals[median_class_index]
lower_median, upper_median = map(float, median_class.split('-'))
frequency_median_class = frequencies[median_class_index]
cum_freq_before_median_class = cum_freq[median_class_index - 1] if median_class_index > 0 else 0
median = lower_median + ((total_freq / 2 - cum_freq_before_median_class) / frequency_median_class) * (upper_median - lower_median)

mode_class_index = np.argmax(frequencies)
mode_class = class_intervals[mode_class_index]
lower_mode, upper_mode = map(float, mode_class.split('-'))
frequency_mode_class = frequencies[mode_class_index]
frequency_prev_mode_class = frequencies[mode_class_index - 1] if mode_class_index > 0 else 0
frequency_next_mode_class = frequencies[mode_class_index + 1] if mode_class_index < len(frequencies) - 1 else 0
mode = lower_mode + ((frequency_mode_class - frequency_prev_mode_class) / ((frequency_mode_class - frequency_prev_mode_class) + (frequency_mode_class - frequency_next_mode_class))) * (upper_mode - lower_mode)

AM = mean

HM = total_freq / np.sum(frequencies / midpoints)

GM = np.exp(np.sum(frequencies * np.log(midpoints)) / total_freq)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Arithmetic Mean (AM): {AM}")
print(f"Harmonic Mean (HM): {HM}")
print(f"Geometric Mean (GM): {GM}")

plt.figure(figsize=(10, 6))
plt.hist(midpoints, bins=len(midpoints), weights=frequencies, color='blue', alpha=0.7, edgecolor='black')

plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')
plt.axvline(median, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median:.2f}')
plt.axvline(mode, color='yellow', linestyle='dashed', linewidth=2, label=f'Mode: {mode:.2f}')

plt.title('Histogram of Grouped Data with Mean, Median, and Mode')
plt.xlabel('Midpoint')
plt.ylabel('Frequency')
plt.legend()

plt.show()
