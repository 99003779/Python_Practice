class Animal:
    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def bark (self):
        print("Dog Barks")

ob = Dog()
ob.bark()
ob.speak()
