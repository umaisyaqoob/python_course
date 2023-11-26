"""Method Overloading:

Method overloading ka matlab hota hai ek hi function ko zyada dfa create krna 
lekin different argumenst (perameters) k sath. """
# with **kargs
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

# with *args

class Calculator2:
    def  soke(self, *args):
        total2 = sum(args)

        return total2


cal2 = Calculator2()
result2 = cal2.soke(1,4,5)
print(result2)

