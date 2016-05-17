# Example.py

def a(my_data):
    print("function a, my_data =  ", my_data)
    my_data = 20
    print("function a, my_data =  ", my_data)

my_data = 10

print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)
