def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

print("Welcome to the Temperature Converter!")
print("Choose a conversion type:")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Celsius to Kelvin")
print("4: Kelvin to Celsius")
print("5: Fahrenheit to Kelvin")
print("6: Kelvin to Fahrenheit")

try:
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp)}°F.")
    elif choice == 2:
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp)}°C.")
    elif choice == 3:
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp}°C is equal to {celsius_to_kelvin(temp)} K.")
    elif choice == 4:
        temp = float(input("Enter temperature in Kelvin: "))
        print(f"{temp} K is equal to {kelvin_to_celsius(temp)}°C.")
    elif choice == 5:
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"{temp}°F is equal to {fahrenheit_to_kelvin(temp)} K.")
    elif choice == 6:
        temp = float(input("Enter temperature in Kelvin: "))
        print(f"{temp} K is equal to {kelvin_to_fahrenheit(temp)}°F.")
    else:
        print("Invalid choice! Please run the program again.")
except ValueError:
    print("Invalid input! Please enter a number.")

