class Cat:
    def meows(self):
        print("Cat Meows")

class Dog:
    def barks(self):
        print("Dog Barks")

class Horse:
    def run(self):
        print("Horses are cool")

class Animal(Cat, Dog, Horse):
    def friends(self):
        print("All are cool")

ob = Animal()
ob.friends()
ob.run()
ob.barks()
ob.meows()