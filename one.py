info = "I live in pakistan" # Regular String
print(info)

name = input("Enter Name\n")
tense = f"My name is {name}" # Format string 
print(tense)

age = input("Enter Age\n")
Age = "I'm {} years old"
print(Age.format(age)) # Format string with format fucntion


info_height = "My height is {height} "
print(info_height.format(height = "5.8cm")) # Format string with format fucntion



designation = input("Enter Designation\n")
company_name = input("Enter Company Name\n")
Designation = "I'm a {1} in {0}"
print(Designation.format(company_name, designation)) # Format string with format fucntion in advence method with index call

sugra_rate = 78
narration = "Today Sugar rate is {:.2f}"  # Format string with format fucntion in advence method with decimals
print(narration.format(sugra_rate)) 
