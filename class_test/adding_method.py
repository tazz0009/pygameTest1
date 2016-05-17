# adding_method.py

class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print("Woof says", self.name)

def main():
    my_dog = Dog()

    my_dog.name = "Spot"
    my_dog.weight = 20
    my_dog.age = 3

    my_dog.bark()

    Dog.bark(my_dog)

if __name__ == "__main__":
    main()
