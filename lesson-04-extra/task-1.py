# Task 1
# Write a Python program to convert temperatures
# to and from Celsius, Fahrenheit.
# Formula : °F = (°C × 9/5) + 32

temperature = float(input("Please enter a temperature value: "))
unit = input("Please enter a temperature unit to which you want to convert (F or C): ")

if unit.upper() == "F":
    temperature_result = temperature * 9 / 5 + 32
elif unit.upper() == "C":
    temperature_result = (temperature - 32) * 5 / 9
else:
    temperature_result = "Please enter a valid temperature unit."

print(f"Result: {temperature_result} {unit.upper()}")
