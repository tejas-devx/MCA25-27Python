# Create a class Rectangle with private attributes length and width Overload '<' operator to compare the area of 2 rectangles.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()


r1 = Rectangle(float(input("Enter length of rectangle 1: ")),
               float(input("Enter breadth of rectangle 1: ")))

r2 = Rectangle(float(input("Enter length of rectangle 2: ")),
               float(input("Enter breadth of rectangle 2: ")))

if r1 > r2:
    print("Rectangle 1 has a larger area.")
elif r1 < r2:
    print("Rectangle 2 has a larger area.")
else:
    print("Both rectangles have equal area.")
