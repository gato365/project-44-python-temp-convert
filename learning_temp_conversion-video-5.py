
## 1: We need two functions to perform conversion
## - C to F
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
## - F to C
def fahrenheit_to_celsius(f):
    return (f - 32) + 5/9


## 2: While Loop - Outer while - Keep asking user to make a choice
while True:
    ## a) Print Options
    print("\nTemperature Converter Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    ## b) Prompt the User to select an Option
    selection = input("Choose your conversion (1-2) or 3 to exit:")


    ## i. Check User's selected option 
    ## - Exit: Break
    if selection == '3':
        print("Exiting Program.")
        break
    
    ## - Conversion: Continue
    if selection not in ['1','2']:
        print("Invalid Choice. Enter 1 or 2 fro proper conversion")

    ## c) Prompt User to enter the number
    ## i. While Loop Check if User's  Input is numeric
    while True:
        try:
            temperature =  float(input("Enter the temperature to convert: "))
            break
        except ValueError:
            print("Invalid Input. Please enter number")
    

    ## d) Print Conversion
    if selection == '1':
        print(f"{temperature} C is {celsius_to_fahrenheit(temperature)} F" )
    elif selection == '2':
        print(f"{temperature} F is {fahrenheit_to_celsius} C")


 