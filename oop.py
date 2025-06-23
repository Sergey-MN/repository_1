import math
from abc import ABC, abstractmethod


# Задание 1. Инкапсуляция
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Задание 2. Наследование
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return self.name, self.position, self.salary


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        res = super().get_info() + (self.programming_language,)
        return res


class Manager(Employee):
    def __init__(self, name, position, salary, employees):
        super().__init__(name, position, salary)
        self.employees = employees

    def get_info(self):
        res = super().get_info() + (self.employees,)
        return res


# Задание 3. Полиморфизм
class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2 / 4

    def perimeter(self):
        return 2 * math.pi * self.radius


lst = [Shape(), Rectangle(1, 2), Circle(5)]

print([(i.area(), i.perimeter()) for i in lst])


# Задание 4. Абстракция и интерфейс
class Transport(ABC):
    @abstractmethod
    def start_engine(cls):
        pass

    @abstractmethod
    def stop_engine(cls):
        pass

    @abstractmethod
    def move(cls):
        pass


class Car(Transport):
    def start_engine(self):
        return 'start car'

    def stop_engine(self):
        return 'stop car'

    def move(self):
        return 'move car'


class Boat(Transport):
    def start_engine(self):
        return 'boat car'

    def stop_engine(self):
        return 'boat car'

    def move(self):
        return 'boat car'


# Задание 5. Множественное наследование
class Flyable:
    def fly(self):
        return "I'm flying!"


class Swimmable:
    def swim(self):
        return "I'm swimming!"


class Duck(Flyable, Swimmable):
    def make_sound(self):
        return "Quack!"


duck = Duck()
print(duck.swim(), duck.make_sound(), duck.fly(), sep='\t')


# (Дополнительно) Задание 6. Комбинированное: Зоопарк
class Animal(ABC):
    @abstractmethod
    def speak(cls):
        pass

    @abstractmethod
    def move(cls):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return 'Move!'


class Birds(Animal, Flyable):
    def speak(self):
        return "Tweet!"

    def move(self):
        pass


class Fish(Animal, Swimmable):
    def speak(self):
        pass

    def move(self):
        pass


lst_animal = [Dog(), Birds(), Fish()]
print([(i.move(), i.speak()) for i in lst_animal])


# Singleton
class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
            cls.instance.initialized = False
        return cls.instance

    def __init__(self):
        if not self.initialized:
            self.logs = []
            self.initialized = True

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs


logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]


# SOLID (S)
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class ReportGen:
    def generate_pdf(self, report: Report):
        print(f"PDF generated {report.title, report.content}")


class ReportSave:
    def save_to_file(self, filename):
        print(f"Saved {filename}")


# SOLID (O)
class PaymentProcessor:
    def pay(self):
        print("pay")


class PayPal(PaymentProcessor):
    def pay(self):
        print("PayPal")


class CreditCard(PaymentProcessor):
    def pay(self):
        print("CreditCard")


class Crypto(PaymentProcessor):
    def pay(self):
        print("Crypto")


# SOLID (L)
class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying!")


class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly.")


# SOLID (I)
class Fly(ABC):
    @abstractmethod
    def fly(self):
        pass


class Run(ABC):
    @abstractmethod
    def run(self):
        pass


class Swim(ABC):
    @abstractmethod
    def swim(self):
        pass


class Animal(ABC):
    pass


class Lion(Animal, Run):
    def run(self):
        print("Lion is running!")

# staticmethod, classmethod, property
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self):
        return self.celsius + 273

    @staticmethod
    def is_negative(celsius):
        return "Yes" if celsius <= 0 else "No"

t = Temperature(20)

print(t.is_negative(-2))

