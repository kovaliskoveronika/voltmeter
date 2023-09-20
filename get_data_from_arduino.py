import time
import serial
from vpython import *
from visualizers.voltmeter import visualize_data


def initialize_serial(port: str, baudrate: int) -> serial.Serial:
    voltage_data = serial.Serial(port, baudrate)
    time.sleep(1)
    return voltage_data


def read_voltage(voltage_data: serial.Serial) -> float:
    while voltage_data.inWaiting() == 0:
        pass
    data_stor = voltage_data.readline()
    data_stor = str(data_stor, "utf-8")
    clean_data = int(data_stor.strip("\r\n"))
    voltage = round(((3.3 / 1023.0) * clean_data), 2)
    return voltage


def update_needle(
        needle: tuple,
        needle_range: float,
        old_pot: int,
        voltage: float,
        scaling_factor: float
) -> int:
    delta_pot = old_pot - int(voltage)
    delta_needle_angle = needle_range * (delta_pot / 1023) * scaling_factor
    needle[0].rotate(
        delta_needle_angle, axis=vector(0, 0, 1), origin=vector(0, -0.4, 0.08)
    )
    return int(voltage)


def main():
    com_port = "com3"
    baud_rate = 115200
    voltage_data = initialize_serial(com_port, baud_rate)

    old_pot = 0
    scaling_factor = 1.0
    needle, needle_range = visualize_data()

    while True:
        voltage = read_voltage(voltage_data)
        old_pot = update_needle(needle, needle_range, old_pot, voltage, scaling_factor)
        rate(10)


if __name__ == "__main__":
    main()
