# temp_conversion_tool.py

# 🌡️ Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # 👤 Ask user for temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Validate numeric input

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print(f"Invalid temperature. Please enter a numeric value. ({ve})")

# 🚀 Run the script
if __name__ == "__main__":
    main()
