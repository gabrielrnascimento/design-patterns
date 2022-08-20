from typing import Callable
from functools import partial



class Dog:
    def __init__(self) -> None:
        self.name = "Dog"

    def bark(self) -> str:
        return "woof!"


class Cat:
    def __init__(self) -> None:
        self.name = "Cat"
    
    def meow(self) -> str:
        return "meow!"
    

class Human:
    def __init__(self) -> None:
        self.name = "Human"

    def speak(self) -> str:
        return "hello!"


class Car:
    def __init__(self) -> None:
        self.name = "Car"

    def make_noise(self, octane_level: int) -> str:
        return f"vroom{'!' * octane_level}"


class Adapter:
    """
    Adapts an object by replacing methods.          \n
    Usage  :                                        \n
    `dog = Dog()`                                   \n
    `dog = Adapter(dog, make_noise=dog.bark)`
    """
    def __init__(self, obj, **adapted_methods: Callable) -> None:
        """ We set the adapted methods in the object's dict. """
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """ All non-adapted calls are passed to the object. """
        return getattr(self.obj, attr)


dog = Dog()
cat = Cat()
human = Human()
car = Car()

dog = Adapter(dog, make_noise=dog.bark)
cat = Adapter(cat, make_noise=cat.meow)
human = Adapter(human, make_noise=human.speak)
car = Adapter(car, make_noise=partial(car.make_noise, octane_level=3))

print(f"a {dog.name} does {dog.make_noise()}")
print(f"a {cat.name} does {cat.make_noise()}")
print(f"a {human.name} does {human.make_noise()}")
print(f"a {car.name} does {car.make_noise()}")