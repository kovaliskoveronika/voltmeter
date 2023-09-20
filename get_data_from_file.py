import time
from vpython import *
from voltmeter import visualize_data
from get_statistic import calculate_statistics

oldPot = 0

# Read data from a text file
with open("voltage_data.txt", "r") as file:
    lines = file.readlines()


scaling_factor = 1.0
needle, needleRange = visualize_data()
voltage = []

for line in lines:
    pot = line.strip()
    deltaPot = oldPot - int(pot)
    deltaNeedleAngle = needleRange * (deltaPot / 1023) * scaling_factor
    needle.rotate(deltaNeedleAngle, axis=vector(0, 0, 1), origin=vector(0, -0.4, 0.08))
    oldPot = int(pot)
    voltage.append(int(pot))
    rate(10)

mean, median, mode, std_dev = calculate_statistics(voltage)

print("\nStatistics:")
print(f"Mean: {mean:.2f} V")
print(f"Median: {median:.2f} V")
print(f"Mode: {mode:.2f} V")
print(f"Standard Deviation: {std_dev:.2f} V")
