import sys

def area_of_circle(radius):
    return 3.14 * radius * radius

if len(sys.argv) == 2:
    r = float(sys.argv[1])
    area = area_of_circle(r)
    print("Area of circle:", area)
else:
    print("Usage: python circle.py <radius>")

