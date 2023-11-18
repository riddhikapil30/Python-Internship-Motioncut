def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def get_user_choice(choices):
    while True:
        user_input = input(f"Choose a conversion type ({', '.join(choices)}): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose a valid conversion type.")

def get_user_value():
    while True:
        user_input = input("Enter the value to convert: ")
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    conversion_types = ["temperature", "length", "weight"]
    conversion_type = get_user_choice(conversion_types)

    if conversion_type == "temperature":
        source_unit = get_user_choice(["celsius", "fahrenheit"])
        target_unit = get_user_choice(["celsius", "fahrenheit"])
        value = get_user_value()

        if source_unit == "celsius" and target_unit == "fahrenheit":
            result = celsius_to_fahrenheit(value)
        elif source_unit == "fahrenheit" and target_unit == "celsius":
            result = fahrenheit_to_celsius(value)
        else:
            result = value  # No conversion needed

    elif conversion_type == "length":
        source_unit = get_user_choice(["meters", "feet"])
        target_unit = get_user_choice(["meters", "feet"])
        value = get_user_value()

        if source_unit == "meters" and target_unit == "feet":
            result = meters_to_feet(value)
        elif source_unit == "feet" and target_unit == "meters":
            result = feet_to_meters(value)
        else:
            result = value  # No conversion needed

    elif conversion_type == "weight":
        source_unit = get_user_choice(["kilograms", "pounds"])
        target_unit = get_user_choice(["kilograms", "pounds"])
        value = get_user_value()

        if source_unit == "kilograms" and target_unit == "pounds":
            result = kilograms_to_pounds(value)
        elif source_unit == "pounds" and target_unit == "kilograms":
            result = pounds_to_kilograms(value)
        else:
            result = value  # No conversion needed

    print(f"{value} {source_unit} is equal to {result} {target_unit}.")

if __name__ == "__main__":
    main()
