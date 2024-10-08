# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5   # Factor for converting Celsius to Fahrenheit
#FAHRENHEIT_OFFSET = 32                  # Offset for Fahrenheit conversion

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main function to demonstrate temperature conversion."""
    # print("Temperature Conversion Tool")

    

    try:
        temperature_input = float(input("Enter the temperature to convert: ").strip())
        #temperature = float(temperature_input)
        #temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        #temperature = float(temperature_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        match unit:
            case 'F':
                celsius = convert_to_celsius(temperature_input)
                print(f"{temperature_input}°F is {celsius}°C")
            case 'C':
                fahrenheit = convert_to_fahrenheit(temperature_input)
                print(f"{temperature_input}°C is {fahrenheit}°F")
            case _:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()