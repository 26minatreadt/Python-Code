from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

# Here, the animal class is an abstract class with
# Specific implementation. Dog provides the concrete   

#Encopsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
# Here, __balance is a priv attribute, and 

class Animal:
    def speak(self):
        return "Animal sound"
    
class Dog(Animal):
    def speak(self):
        return "Bark"
    
class Cat(animal):
    def sound(self):
        return "Meow"
    
def make_sound(animal):
    print(animal.sound)

make_sound(Cat()) #output: Meow
make_sound(Dog()) #output: Bark
