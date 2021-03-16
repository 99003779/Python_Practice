class CAR:

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display(self):
        print(self.model, self.year)


c1 = CAR("Jaguar", 2019)

c1.display()
