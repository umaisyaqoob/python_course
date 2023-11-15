# USER INPUT 

username = input("Enter Username:")
print("User Name is:" + username)



try:
    # Code that might raise an exception
    result = 10 / 2  # Division by zero will raise an exception
except TypeError:
    # Handle the exception
    print("Error: Division by zero")
else:
    print("Division successful. Result:", result)
finally:
    print("Execution Successfull")



    #Practice Section
    
    #1st

try:
    number = int(input("Enter Number: "))
    ok = 10 / number
except ZeroDivisionError:
    print("Error: Divisio error zero")
else:
    print("Division Successfull", ok)

    # 2nd

try:

    list = []
    num1 = int(input("Enter Number 1\n"))
    num2 = int(input("Enter Number 2\n"))
    num3 = int(input("Enter Number 3\n"))
    num4 = int(input("Enter Number 4\n"))
    num5 = int(input("Enter Number 5\n"))

    conv1 = list.append(num1)
    conv2 = list.append(num2)
    conv3 = list.append(num3)
    conv4 = list.append(num4)
    conv5 = list.append(num5)
    khan = sum(list)
    
except ValueError:
    print("Error: Please enter integer value")
else:
    print("your Programme is correct and final sum of list is  = ", khan )
finally:
    print("Operation Successfull")

