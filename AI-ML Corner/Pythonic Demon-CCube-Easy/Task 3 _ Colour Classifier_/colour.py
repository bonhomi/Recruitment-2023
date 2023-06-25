def classify_color(color):
    red, green, blue = color

    if red > green and red > blue:
        return "Red"
    elif blue > red and blue > green:
        return "Blue"
    elif green > red and green > blue:
        return "Green"
    else:
        return "Unclassified"

red=int(input())
green=int(input())
blue=int(input())
color = (red,green,blue)
classification = classify_color(color)
print("Color:", color)
print("Classification:", classification)