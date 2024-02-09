def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    print("\nTemperature Converter Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose your conversion (1-2) or 3 to Exit: ")

    if choice == '3':
        print("Exiting the program.")
        break

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius.")
        continue

    # while True:
    #     try:
    temperature = float(input("Enter the temperature to convert: "))
        #     break
        # except ValueError:
        #     print("Invalid input. Please enter a number.")

    if choice == '1':
        print(f"{temperature}°C is {celsius_to_fahrenheit(temperature):.2f}°F")
    elif choice == '2':
        print(f"{temperature}°F is {fahrenheit_to_celsius(temperature):.2f}°C")
