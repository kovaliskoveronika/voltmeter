from vpython import vector, rate
from visualizers.voltmeter import visualize_data
from get_statistic import calculate_statistics
from typing import List


def read_voltage_data(file_path: str) -> List[int]:
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [int(line.strip()) for line in lines]


def update_needle(
        needle: tuple,
        needle_range: float,
        voltage_data: List[int],
        scaling_factor: float
) -> None:
    old_pot = 0
    for pot in voltage_data:
        delta_pot = old_pot - pot
        delta_needle_angle = needle_range * (delta_pot / 1023) * scaling_factor
        needle[0].rotate(delta_needle_angle, axis=vector(0, 0, 1), origin=vector(0, -0.4, 0.08))
        old_pot = pot
        rate(10)


def main():
    file_path = "data/voltage_data.txt"
    scaling_factor = 1.0
    needle, needle_range = visualize_data()
    voltage_data = read_voltage_data(file_path)

    update_needle(needle, needle_range, voltage_data, scaling_factor)

    mean, median, mode, std_dev = calculate_statistics(voltage_data)

    print("\nStatistics:")
    print(f"Mean: {mean:.2f} V")
    print(f"Median: {median:.2f} V")
    print(f"Mode: {mode:.2f} V")
    print(f"Standard Deviation: {std_dev:.2f} V")


if __name__ == "__main__":
    main()
