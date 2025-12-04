# Create a class Person(name,age) with a constrctor and a method display().Create a class Employee(EmpID) from Person,override display() to include the ID.Create a derived class Faculty(department) from Employee,override display() to include the department.Create a seperate class Researcher with a method can_do_research() that returns a string indicating the person can conduct research.Create a final class Professor which inherits from Faculty and Researcher.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)
        self.empid = empid

    def display(self):              # overriding
        super().display()
        print("Employee ID:", self.empid)


class Faculty(Employee):
    def __init__(self, name, age, empid, dept):
        super().__init__(name, age, empid)
        self.dept = dept

    def display(self):              # overriding
        super().display()
        print("Department:", self.dept)


class Researcher:
    def can_do_research(self):
        return "This person can conduct research."


class Professor(Faculty, Researcher):
    def __init__(self, name, age, empid, dept):
        Faculty.__init__(self, name, age, empid, dept)

    def display(self):
        super().display()
        print(self.can_do_research())



name = input("Enter name: ")
age = int(input("Enter age: "))
empid = input("Enter employee ID: ")
dept = input("Enter department: ")

p = Professor(name, age, empid, dept)
p.display()
