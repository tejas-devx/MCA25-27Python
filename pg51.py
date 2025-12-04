# Create Rectangle class with attributes length, breadth — find area & perimeter — compare two rectangles by their area.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r1 = Rectangle(float(input("Enter length of rectangle 1: ")),
               float(input("Enter breadth of rectangle 1: ")))

r2 = Rectangle(float(input("Enter length of rectangle 2: ")),
               float(input("Enter breadth of rectangle 2: ")))


print("Area of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())

if r1.area() > r2.area():
    print("Rectangle 1 is bigger.")
elif r1.area() < r2.area():
    print("Rectangle 2 is bigger.")
else:
    print("Both rectangles have equal area.")
