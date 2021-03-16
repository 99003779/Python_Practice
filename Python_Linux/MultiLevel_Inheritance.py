class Animal:
    def speaks(self):
        print("Animal Speaks")

class Cat(Animal):
    def meows(self):
        print("Cat Meows")

class Dog(Cat):
    def friends(self):
        print("Cat and Dog are friends")

ob = Dog()
ob.friends()
ob.meows()
ob.speaks()