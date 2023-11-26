                                        # Learning Example

# class Car:
#     def __init__(self, make, model):
#         self.__make = make  # private member
#         self._model = model  # protected member
#         self.speed = 0  # public member

#     def accelerate(self):
#         self.speed += 10
#         return f"Accelerating! Current speed: {self.speed}"

#     def brake(self):
#         self.speed -= 5
#         print(f"Braking! Current speed: {self.speed}")

#     def get_make(self):
#         return self.__make

#     def set_make(self, make):
#         self.__make = make

# # Creating an object of the Car class
# car = Car("Toyota", "Camry")

# # Accessing public member
# print(f"Car speed: {car.speed}")

# # Accessing protected member
# print(f"Car model: {car._model}")

# # Accessing private member through getter method
# print(f"Car make: {car.get_make()}")

# # Modifying private member through setter method
# car.set_make("Honda")
# print(f"Modified Car make: {car.get_make()}")

# print(f"{car.accelerate()}")

                                      # Practice code


# Tips
# private variable  __name  **(Ye variable direct access ni kr skty bss method k through hi kr skty hain)**
# protected variable  _name  **(Ye variable hm direct access kr skty hain lekin hmy direct access ni krna chahiye ye developers ki asani k liye hota hai code ko smjhna asan hota hai k ye variable direct access ni krna chahiye)**
# public variable  name **(Ye variable jb mrzi access kr skty hain)**


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age



person = Person("Umais", 23) 
print(person.get_name()) # yha mei method yani function k through private variable ko access kr rha hu direct access ni kr skta
# print(person.__name)    **(agr mei ye code un comment kru ga to error ay ga kiyon k mei private variable ko access kr rha hu jo k access ni hota esi liye error arha hai)**  
person.set_name("Amir")
print(person.get_name())


name = "umais"
result = name[::-1]
print(result)


        




