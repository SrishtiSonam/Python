# Designing concept



# 1. Basic Classes and Objects 
#       - Create a car class with attributes like brand and model. Also create instances of this class. 

# class Car:
#     brand = None
#     model = None
# my_car = Car()
# print(my_car)               # <__main__.Car object at 0x000001DA60547770>


# Blank form
class Car:
    total_car = 0
    def __init__(self, brand, model):                   # Constructor
        self.__brand = brand                        # MAking is private
        self.__model = model
        Car.total_car += 1
        # self.total_car += 1           -       Other way
    def printName(self):
        self.fullname = f"{self.__brand} {self.__model}"
        print(self.fullname)
    def get_brand(self):
        return self.__brand + "!"
    def here_model(self):
        return self.__model
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_discription():
        return "4 wheeler."

    @property
    def model(self):
        return self.__model
    

# # my_car = Car("Toyota", "Corolla")   -   without self    -   TypeError: Car.__init__() takes 2 positional arguments but 3 were given

my_car = Car("Toyota", "Corolla") 
# print("My car object is", my_car,".\nIts brand name is", my_car.brand,"and model is", my_car.model)
# # My car object is <__main__.Car object at 0x0000026C54A77D10> .
# # Its brand name is Toyota and model is Corolla

my_new_car = Car("Tata", "Safari")



# # 2. Class Method and Self
# #       - Add a method to the Car class that displays the full name of the car (brand and model)

# my_new_car.printName()                                  # Tata Safari



# 3. Inheritance
#       - Create an ElecticCar class that inherits from the Car class with additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                      # Going to upper class
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electricity"

my_tesla = ElectricCar("Tesla", "Model S", "*5kWh")
my_tesla.printName()                                        # Tesla Model S



# # 4. Encapsulation 
# #       - Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.       {   brand not in a access to all  -  accessed through a method    -   getter and setter   }

# print(my_tesla.get_brand())
# # print(my_tesla.__brand)                     # 'ElectricCar' object has no attribute '__brand' as it is private.
# print(my_tesla.here_model())
# # print(my_tesla.__model)                       # 'ElectricCar' object has no attribute '__model'



# # 5. Polymorphism       -       It also depends on fuel type 
# #       - define a method fuel_type in both Car and ElectricCar classes, but with different behaviour.

# print(my_new_car.fuel_type())
# print(my_tesla.fuel_type())



# # 6. Class Variables
# #       - Add a class variable to Car that keeps the track of no. of cars created.

# print(my_tesla.total_car)
# test = Car("test", "test")
# print(test.total_car)
# Car("noname", "noname")             #   Created without any name
# print(Car.total_car)



# # 7. Static Method ########################################################################
# #       - Add a static method to the Car class that return the general discription of a car.
# #       - Static Methods : Method that belongs to the class rather than an instance / object of a class. 

# print(Car.general_discription())                # 4 wheeler.
# print(my_tesla.general_discription())           # 4 wheeler.



# # 8. Property Decorators
# #       - Use a property decorator in the Car class to make the model attribute read only. 

# my_car.fullname = "Hello Hello"
# print(my_car.fullname)                      # Hello Hello
# my_car.printName()                          # Toyota Corolla
# print(my_car.model)                 # No over writing



# # 9. Class Inheritance and isinstance() Function
# #       - Demonstate the use of isinstance() to check if my_tesla is instance of Car and ElectricCar.

# print(isinstance(my_tesla, Car))                        # True
# print(isinstance(my_tesla, ElectricCar))                        # True
# print(isinstance(my_car, Car))                        # True
# print(isinstance(my_car, ElectricCar))                        # False



# # 10. Multiple Inheritance
# #       - Create two classes Battery and Engine, and let the ElectricCarTwo class inherit from both.

# class Battery:
#     def battery_info(self):
#         return "This is battery class."

# class Engine:
#     def engine_info(self):
#         return "This is engine class."

# class ElectricCarTwo(Battery, Engine, Car):
#     def whole_info(self):
#         return "This is whole."
    
# ECT = ElectricCarTwo("GGG", "JJJ")
# print(ECT.whole_info())
# print(ECT.engine_info())
# print(ECT.battery_info())
# ECT.printName()