def temperature_convert(temperature, unit):
    if unit.upper() == "F":
        temperature_result = temperature * 9 / 5 + 32
    elif unit.upper() == "C":
        temperature_result = (temperature - 32) * 5 / 9
    else:
        temperature_result = "Please enter a valid temperature unit."

    print(f"Result: {temperature_result:.2f} {unit.upper()}")


print(__name__)
