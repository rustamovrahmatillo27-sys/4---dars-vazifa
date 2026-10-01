from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __new__(cls, *args, **kwargs):
        if cls is Vehicle:
              raise TypeError("Vehicle abstrakt class uni yaratib bo'lmaydi")
        return super().__new__(cls)

    def __init__(self, marka, model, yil, tezlik):
        self._brand = marka
        self._model = model
        self._year = yil
        self._speed = tezlik


    @property
    def speed(self):
         return self.speed
    @abstractmethod
    def start(self):
         pass

    @abstractmethod
    def move(self):
         pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self._brand} {self._model}, {self._year}-yil, tezlik: {self._speed} km/soat"
 
    def __repr__(self):
        return f"{self.__class__.__name__}({self._brand}, {self._model}, {self._year}, {self._speed})"
 
    def __bool__(self):
        return self._speed > 0
 
    def __eq__(self, other):
        return self._speed == other._speed
 
    def __ne__(self, other):
        return self._speed != other._speed
 
    def __gt__(self, other):
        return self._speed > other._speed
 
    def __ge__(self, other):
        return self._speed >= other._speed
 
    def __lt__(self, other):
        return self._speed < other._speed
 
    def __le__(self, other):
        return self._speed <= other._speed


class Car(Vehicle):
    def start(self):
        print("Moshina ot oldi")

    def move(self):
        print("Moshina yurmoqda")


class Motorcycle(Vehicle):
    def start(self):
        print("Mototsikl o't oldi")
 
    def move(self):
        print("Mototsikl yurmoqda")
 
 
class Truck(Vehicle):
    def start(self):
        print("Yuk mashinasi ot oldi")
 
    def move(self):
        print("Yuk mashinasi yuk tashimoqda")


car = Car("Chevrolet", "Malibu", 2025, 190)
moto = Motorcycle("Kawasaki", "Ninja 400", 2018, 190)
truk = Truck("Man", "Man TGX", 2016, 120)

vehicles = [car, moto, truk]
 
for vehicle in vehicles:
    print(vehicle)
    print(repr(vehicle))
    vehicle.start()
    vehicle.move()
 
print(bool(car))
 
print(car == moto)
print(car != truk)
 
print(car > moto)
print(truk <= car)

    