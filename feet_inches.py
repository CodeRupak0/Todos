feet_inches=input("Enter feet and inches:")

def conversion(feet_inches):
    parts = feet_inches.split(" ")  # its splits the strings into many parts at the place of space.
    feet= float(parts[0])   # conversion of string into float value for conversion.
    inches= float(parts[1])
    meters= feet *0.3048 + inches*0.0254
    return (f"{feet} feet and {inches} inches is equal to {meters} meters")

print(conversion(feet_inches))