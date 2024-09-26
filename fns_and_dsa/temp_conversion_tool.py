# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5   # Factor for converting Celsius to Fahrenheit
FAHRENHEIT_OFFSET = 32                  # Offset for Fahrenheit conversion

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    """Main function to demonstrate temperature conversion."""
    # print("Temperature Conversion Tool")

    temperature_input = input("Enter the temperature to convert: ").strip()

    try:
        temperature = float(temperature_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()