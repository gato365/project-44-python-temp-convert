# try:
#     temperature =  float(input("Enter temperature: "))
#     print(temperature)
# except ValueError:
#     print("Invalid Input. Please enter a number.")
    
try:
    x = float(input("Enter Numerator: "))
    y = float(input("Enter Denominator: "))
    z = x/y
    print(z)
except ZeroDivisionError:
    print("Error. Dividing by 0 is not allowed.")