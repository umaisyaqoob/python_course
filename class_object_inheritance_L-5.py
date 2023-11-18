# "Class" and "Objects" , "Constructor" Concepts

class One:                 # Here "One" is Class
    def __init__(self, name, city):
        self.s = name
        self.city = city

    def practice(self, fn, ln):
        self.fname = fn
        self.lname = ln
        print(self.fname)
        print(self.lname)



one = One("Umais", "Yaqoob")  # one is a object  / One() is a constructor
print(one.practice(1, "Practice")) # practice method k variables mujy usi method mei pehly print krwany pryn gy isr bs arug du gaa bss or kam kr jay ga
print(one.s) # idr mei object k through __init__ function (method) k variable (instance) ko direct call kr rha hu kiyon k object bnaty time __init__
# method auto chlta hota hai jb object create ho rha ha to __init__ khud chl rha hai to mujy init ko call krwany ki zrurt ni hai
# bss __init k variables ko call krwau ga print ho jayn gy__


# Inheritance Concepts

class Two(One):
    def __init__(self, name, city):
        super().__init__(name, city)
        

        def practice(self, fn, ln , age):
            self.fname = fn
            self.fname = ln
            self.Age = age
            print(self.Age)


two = Two("Tesla", "Mustang")

two.practice("Umais", "yaqoob")






