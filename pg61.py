# Create a class complex with private attributes real & imaginary parts.Overload '>==' operator to find greatest no.

class Complex:
    def __init__(self, real, imag):
        self.__r = real
        self.__i = imag

    def magnitude(self):
        return (self.__r**2 + self.__i**2) ** 0.5

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()


c1 = Complex(3, 4)     # magnitude = 5
c2 = Complex(1, 7)     # magnitude ≈ 7.07

if c1 >= c2:
    print("c1 is greater")
else:
    print("c2 is greater")
