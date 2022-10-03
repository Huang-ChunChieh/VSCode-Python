class Elevator:
    def __init__(self, starting_floor):
        self.make = "The Elevator Company"
        self.floor = starting_floor

#To create the obj.

elevator = Elevator(1)
print(elevator.make) # "the Elevator Company"
print(elevator.floor) # 1

# self錯誤用法
# class Car:
#     def __init__():
#         self.color = "Red" # ends up on the object
#         make = "Mercedes" # becomes a local variable in the constructor     正確:self.make = "Mercedes"

# car = Car()
# print(car.color) # "Red"
# print(car.make) # would result in an error, `make` does not exist on the object