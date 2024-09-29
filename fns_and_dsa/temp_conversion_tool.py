FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  


def convert_to_celsius(fahrenheit):

  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius


def convert_to_fahrenheit(celsius):
 
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit


if __name__ == "__main__":
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
      break
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

  if unit == 'C':
    converted_temperature = convert_to_fahrenheit(temperature)
    unit_label = "°C"
    converted_unit_label = "°F"
  elif unit == 'F':
    converted_temperature = convert_to_celsius(temperature)
    unit_label = "°F"
    converted_unit_label = "°C"
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")
    exit()

  print(f"{temperature}{unit_label} is {converted_temperature:.2f}{converted_unit_label}")
