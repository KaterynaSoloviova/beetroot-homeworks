from temperature.module1 import temperature_convert

def test_temperature_convert():
    temperature_convert(35, 'F')
    temperature_convert(130, 'C')

if __name__ == "__main__":
    test_temperature_convert()
