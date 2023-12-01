"""Yahan Info class Person abstract class se inherit ho rahi hai.
Ismein area method ko implement karna zaroori hai, warna aapko error milega."""

# | Yhi main point hai es mei |

from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def personal(self):
        pass

class Info(Person):
    def __init__(self, name):
        self.__name = name

    def personal(self):
            return f'My name is {self.__name}'
    

info = Info("Muhammad Umais")

print(info.personal())