# class Animal:
#     def make_sound(self,s):
#         print(s)
# class Horse(Animal):
#     pass

# class Parent:
#     def go(self, s):
#         print(s)
# class Kid(Parent):
#     pass

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor

# class Car:
#     @classmethod
#     def stop(cls):
#         print('Машина остановилась')
#
# Car.stop()

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#         @property
#         def area(self):
#             return self.width * self.height
#
# rectangle = Rectangle(4,5)
# print(rectangle.area)
#
# rectangle.width = 6
# print(rectangle.area)


# class Worker:
#     def __init__(self, name, job):
#         self.name = name
#         self.job = job
#
#
# class Worker2(Worker):
#     def __init__(self, name, job):
#         super().__init__(name, job)
#         return name

class Player:
    def __init__(self, strength, number):
        self.strenght = strength
        self.number = number

class Nap(Player):
    def __init__(self, strength, number, hands):
        super().__init__(strength, number)
        self.hands = hands


class Zach(Player):
    def __init__(self, strength, number, legs):
        super().__init__(strength, number)
        self.legs = legs


class P_Zach(Player):
    def __init__(self, strength, number, right):
        super().__init__(strength, number)
        self.right = right


class Vratar(Player):
    def __init__(self, strength, number, speed):
        super().__init__(strength, number)
        self().speed = speed


