def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

flag = True
while flag:
    print("\nTemperature Converter Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose your conversion (1-2) or 3 to Exit: ")

    if choice == '3':
        print("Exiting the program.")
        flag = False

    elif choice in ['1', '2']:
        valid_input = False
        while not valid_input:
            temperature = input("Enter the temperature to convert: ")
            if temperature.replace('.', '', 1).isdigit():
                temperature = float(temperature)
                valid_input = True
            else:
                print("Invalid input. Please enter a number.")

        if valid_input:
            if choice == '1':
                print(f"{temperature}°C is {celsius_to_fahrenheit(temperature):.2f}°F")
            elif choice == '2':
                print(f"{temperature}°F is {fahrenheit_to_celsius(temperature):.2f}°C")

    else:
        print("Invalid choice. Please enter 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius.")


"""In this version, the `flag` variable is used to control the outer loop. If the user enters '3' for the conversion choice, the program sets `flag` to `False`, which ends the loop and exits the program. The `valid_input` variable is used to control the inner loop. If the user enters a valid number for the temperature, the program sets `valid_input` to `True`, which ends the inner loop and allows the program to perform the chosen conversion. If the user enters a non-numeric value for the temperature, the program prints an error message and then asks for the temperature again, without going back to the conversion choice. This should give you the behavior you're looking for. I hope this helps! Let me know if you have any other questions. 😊"""