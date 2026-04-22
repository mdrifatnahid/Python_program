# Area of a Sector
import math

print("Area of a Sector:- ")

radius = float(input("Enter radius : "))
thita = float(input("Enter Thita (in degrees): "))

# Convert degrees to radians
thita_radians = math.radians(thita)

area = 0.5 * radius**2 * thita_radians

print("The area of the Sector is ", area)