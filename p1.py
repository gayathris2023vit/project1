print("Temperature Converter Options:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Select an option (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # Formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

else:
    print("Invalid choice. Please select 1 or 2.")
