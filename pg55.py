# Create a class Publisher(name).Derive a class Book(title,author) from Publisher.Derive a class Python(prce,no_of_pages) from Book.Write a program that displays information about a Python book.Use base class constructor invocation and method overriding.

class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)      
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):               
        super().display()
        print("Price:", self.price)
        print("No. of Pages:", self.pages)


pub = input("Enter publisher name: ")
title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter price: "))
pages = int(input("Enter no. of pages: "))

obj = Python(pub, title, author, price, pages)
obj.display()

# obj = Python("O'Reilly", "Python Cookbook", "David Beazley", 899, 820)
# obj.display()
