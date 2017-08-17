"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    def fahrenheit_to_celsius(fahrenheit):
        celsius = 5 / 9 * (fahrenheit - 32)
        return celsius

    def celsius_to_fahrenheit(celsius):
        fahrenheit = celsius * 9.0 / 5 + 32
        return fahrenheit

    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            celsius_to_fahrenheit(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(fahrenheit)

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            fahrenheit_to_celsius(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(celsius)

        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
