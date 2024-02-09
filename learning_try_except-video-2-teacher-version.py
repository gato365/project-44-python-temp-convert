



try:
    temperature = float(input("Enter temperature: "))
    print(temperature)
except ValueError:
    print("Invalid Input. Please enter a number")



try:
    x = float(input("Enter a numerator: "))
    y = float(input("Enter a denominator: "))
    z = x / y
except ZeroDivisionError:
    print("Error: Division by zero. Setting result to 0.")
    z = 0

print(f"Result: {z}")