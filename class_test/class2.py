# class2.py

class ClassA():
    def __init__(self):
        self.y = 3

class ClassB():
    x = 7

def main():
    a = ClassA()
    b = ClassB()

    print(b.x)
    print(ClassB.x)

    print(a.y)
    print(ClassA.y)

if __name__ == "__main__":
    main()
