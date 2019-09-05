HEX_ADDRESS_TO_NAME = {"blue 1": "#0000ff", "GreenYellow": "#adff2f", "MediumSpringGreen": "#00fa9a",
                       "orchid2": "#ee7ae9", "PaleTurquoise1": "#bbffff", "PapayaWhip": "#ffefd5", "purple4": "#551a8b",
                       "red1": "#ff0000", "YellowGreen": "#9acd32", "tomato3": "#cd4f39"}

colour = (input("Enter colour name: ")).lower()
while colour != "":
    if colour in HEX_ADDRESS_TO_NAME:
        print(HEX_ADDRESS_TO_NAME[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")
