# 1. Selective import of module from package
from graphics import rectangle

# 2. Selective import of circle functions
from graphics.circle import area as c_area, perimeter as c_perimeter

# 3. Importing from subpackage
from graphics.threeD_graphics import cuboid
from graphics.threeD_graphics.sphere import area as sphere_area

print("Rectangle Area:", rectangle.area(10, 5))
print("Rectangle Perimeter:", rectangle.perimeter(10, 5))

print("\nCircle Area:", c_area(7))
print("Circle Perimeter:", c_perimeter(7))

print("\nCuboid Surface Area:", cuboid.surface_area(2, 3, 4))
print("Cuboid Perimeter:", cuboid.perimeter(2, 3, 4))

print("\nSphere Area:", sphere_area(5))



# package qstn