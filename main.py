# 1. Using self
print("__________________________________________________")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Aneeq", 90)
s1.display()
print("__________________________________________________")


# 2. Using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

c1 = Counter()
c2 = Counter()
Counter.show_count()
print("__________________________________________________")


# 3. Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car has started.")

my_car = Car("Porsche")
print(my_car.brand)
my_car.start()
print("__________________________________________________")


# 4. Class Variables and Class Methods

class Bank:
    bank_name = "ABC Bank"

    def display(self):
        print("Bank Name:", Bank.bank_name)

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


# Dono objects banaye

bank1 = Bank()
bank2 = Bank()

print("Before changing the bank name:")
bank1.display()  
bank2.display() 

# Bank name change kiya
Bank.change_bank_name("XYZ Bank")
print("Bank name has been changed to: XYZ Bank")

print("\nAfter changing the bank name:")
bank1.display() 
bank2.display()  
print("__________________________________________________")



# 5. Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))
print("__________________________________________________")


# 6. Constructors and Destructors

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

l = Logger()
del l
print("__________________________________________________")


# 7. Access Modifiers

class Employee:
    def __init__(self):
        self.name = "Aneeq"
        self._salary = 50000
        self.__ssn = "123-45-6789"

emp = Employee()
print(emp.name)          # Public
print(emp._salary)       # Protected (still accessible)
# print(emp.__ssn)       # Will raise error
print(emp._Employee__ssn)  # Accessing private
print("__________________________________________________")


# 8. The super() Function

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Ali", "Math")
print(t.name, t.subject)
print("__________________________________________________")


# 9. Abstract Classes and Methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

r = Rectangle(5, 4)
print(r.area())
print("__________________________________________________")


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

d = Dog("Buddy", "Labrador")
d.bark()
print("__________________________________________________")


# 11. Class Methods

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)
print("__________________________________________________")


# 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))
print("__________________________________________________")


# 13. Composition

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start()
print("__________________________________________________")


# 14. Aggregation

class Department:
    def __init__(self, employee):
        self.employee = employee

class Employee:
    def __init__(self, name):
        self.name = name

emp = Employee("Ali")
dept = Department(emp)
print(dept.employee.name)
print("__________________________________________________")


# 15. MRO and Diamond Inheritance

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # MRO: D -> B -> C -> A
print("__________________________________________________")


# 16. Function Decorators

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
print("__________________________________________________")


# 17. Class Decorators

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.greet())
print("__________________________________________________")


# 18. Property Decorators

class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

prod = Product()
prod.price = 50
print(prod.price)
del prod.price
print("__________________________________________________")


# 19. callable() and __call__()


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

m = Multiplier(3)
print(callable(m))
print(m(5))


print("__________________________________________________")


# 20. Custom Exception


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Age is valid.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)


print("__________________________________________________")


# 21. Custom Iterable


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)
print("__________________________________________________")
