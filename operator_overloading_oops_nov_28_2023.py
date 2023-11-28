"""Bilkul, bhai! Python mein operator overloading ka matlab hota
hai ke hum apne banaye gaye objects ke liye operators ke behavior
ko customize kar sakte hain. Iske liye humein apne class mein kuch
special methods define karne hote hain. Ye methods humare class ke
objects ke liye specific operations ko handle karte hain."""

"""Bilkul, main detail mein samjhaunga. Jab aap + operator ka
use karte hain, Python internally __add__ method ko call karta
hai, agar woh method available hai. Yeh method aapke class mein
define hota hai aur aap ise override karke customize kar sakte hain."""

"""
Operator Overloading ka Concept:

    Python mein, aap operators ko customize kar sakte hain. Har ek operator
    ke liye ek special method hota hai, jise "dunder" method kehte hain 
    (Double Under, kyunki isme double underscores hote hain). Jaise ki
    + operator ke liye __add__ method hai.

Internally Method Call:

    Jab aap kisi object par + operator use karte hain, Python dekhta hai 
    ki us object ke class mein __add__ method define hai ya nahi. Agar hai, 
    toh woh method ko call karta hai.

Method Arguments:

    __add__ method ke do arguments hote hain - self aur other. 
    self woh object hai jis par 

    aapne operator use kiya hai, aur other woh object hai jo aapne 
    add kiya ja raha hai.

python"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Addition operator (+) ko customize karne ke liye special method
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y * other.y)
        else:
            raise ValueError("Unsupported operand type for +")

  

    # String representation (str()) ko customize karne ke liye special method
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Example istemal
point1 = Point(1, 2)
point2 = Point(3, 4)

# Overloaded addition operator ka istemal
result = point1 + point2
print(result)  # Output: Point(4, 6)

# Overloaded equality operator ka istemal
print(point1 == point2)  # Output: False
print(point1 == Point(1, 2))  # Output: True


