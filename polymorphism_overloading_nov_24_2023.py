"""Method Overloading:

Method overloading ka matlab hota hai ek hi function ko zyada dfa create krna 
lekin different argumenst (perameters) k sath. """

class Calculator:
    def  soke(self, **kargs):
        total = kargs

        return total


cal = Calculator()
result = cal.soke(name="umais")
print(result)

cal = Calculator()
result = cal.soke(name="Ali", city="Fsd")
print(result)