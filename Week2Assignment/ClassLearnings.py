"""
1) Define a class Person with attributes name and age.
   Create an instance and print its attributes.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Sumit", 25)
print(p.name)
print(p.age)


"""
2) Write a Python class BankAccount with attributes:
   account_number, balance, customer_name
   Methods: deposit(), withdraw(), check_balance()
"""
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print("Current balance:", self.balance)

acc = BankAccount("12345", "Sumit", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.check_balance()


"""
3) Create a class Book with class method from_string() 
   that creates a Book instance from a string.
   book = Book.from_string("Python Programming, John Doe")
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(",")
        return cls(title.strip(), author.strip())

book = Book.from_string("Python Programming, John Doe")
print(book.title)
print(book.author)


"""
4) Create a base class Animal with method sound().
   Create subclasses Dog and Cat that override the sound() method.
"""
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.sound()
c.sound()


"""
5) Write code to perform multiple inheritance.
"""
class Father:
    def father_feature(self):
        print("Feature from Father")

class Mother:
    def mother_feature(self):
        print("Feature from Mother")

class Child(Father, Mother):
    def child_feature(self):
        print("Feature from Child")

baby = Child()
baby.father_feature()
baby.mother_feature()
baby.child_feature()
