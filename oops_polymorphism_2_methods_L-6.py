def print_fun(*args):
    for rec in args:
        print(rec)



print_fun(1,2,3,4,5,6)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name='John', age=25)
# Output: name: John
#         age: 25
