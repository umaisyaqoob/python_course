"""Meta classes Python mein advanced object-oriented programming ka ek mazboot concept hain.
Yeh class ko define karte hain jo doosri classes ki behavior control karti hai. 
Meta classes classes ko create, modify, aur control karne mein istemal hoti hain. 
Meta classes ka use karke aap class creation aur behavior customization mein advanced 
level par intervene kar sakte hain."""


class Meta(type):
    def __new__(cls, name, bases, dct):
        # Customizing class blueprint
        dct['custom_attribute'] = 'This is a custom attribute'
        dct['custom_attribute'] = 'Umais'
        dct['number']           = 234
        return super().__new__(cls, name, bases, dct)

# Class creation using Meta as its metaclass
class MyClass(metaclass=Meta):
    existing_attribute = 'Existing attribute'

    def existing_method(self):
        return f"{self.existing_attribute} method is called."

# Creating an instance of MyClass
my_instance = MyClass()

# Accessing attributes and calling methods
print(my_instance.existing_attribute)  # Output: Existing attribute
print(my_instance.custom_attribute)    # Output: This is a custom attribute
print(my_instance.number)    # Output: This is a custom attribute
print(my_instance.existing_method())   # Output: Existing attribute method is called.
