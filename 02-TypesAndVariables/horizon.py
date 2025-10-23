import math

height = int(input("Input your height: "))/100

height_beach = 0
height_hotel = 20

d1 = 3.57 * math.sqrt(height_beach + height)
d2 = 3.57 * math.sqrt(height_hotel + height)

print(f"Beach: {d1} + Hotel: {d2}")
