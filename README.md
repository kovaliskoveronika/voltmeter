# Voltmeter

This project was created for measuring voltage using Arduino as a measuring device. Here you find two files to measure voltage.

### Get_data_from_arduino

Here you will find a Python script, that catches Arduino data and displays it.

### Get_data_from_file

This script visualizes data, which you can store in a Txt file, in case you don't have access to Arduino.

## Check it out

[Simulate Arduino scheme](https://wokwi.com/projects/376382958568751105)

## Installations
Python must be installed

### Clone the repository
```python
git clone https://github.com/kovaliskoveronika/voltmeter.git
```
### Create a virtual environment
```python
python3 -m venv venv
```
for Windows
```python
venv/Scripts/activate
```
for Linux/MacOS
```python
source env/bin/activate
```
### Install requirements
```python
pip install -r requirements.txt
```

## Demo

Voltmeter must automatically open in your browser and must look like this
![Voltmeter](https://github.com/kovaliskoveronika/voltmeter/blob/main/screenshots/voltmeter.PNG)

In the console, you will get statistical data(this example is for file statistic_data.txt)

![Statistic](https://github.com/kovaliskoveronika/voltmeter/blob/main/screenshots/statistic_data.PNG)
