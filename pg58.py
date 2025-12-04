# Create class Currency(amount, unit). Overload ‘==’ operator to check equality

class Currency:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit


c1 = Currency(100, "INR")
c2 = Currency(100, "INR")

if c1 == c2:
    print("Currencies are equal.")
else:
    print("Currencies are not equal.")
