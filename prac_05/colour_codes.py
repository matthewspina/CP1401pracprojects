COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "aquamarine1": "7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc",
                "black": "#000000", "blue1": "#0000ff"}

colour = str(input("Enter colour:"))
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is",COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = str(input("Enter colour:"))


