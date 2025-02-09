import math  # Import the math module to use mathematical functions like pi

# Ask the user to input the radius and convert it to a float
radius = float(input("Write Radius her --> "))

# Calculate the area of the circle using the formula: π * radius^2
areal = math.pi * radius**2

# Calculate the circumference of the circle using the formula: 2 * π * radius
omkretsen = 2 * math.pi * radius

# Print the area of the circle
print(f"Arealet er {areal}")

# Print the circumference of the circle
print(f"Omkretsen er {omkretsen}")
