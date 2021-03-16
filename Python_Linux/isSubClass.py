class Addition:
    def add(self,num1,num2):
        return num1 + num2

class Subtraction:
    def sub(self, num1,num2):
        return num1 - num2

class Calculation(Addition,Subtraction):
    def Cal(self, num1,num2):
        return num/num2

ob = Calculation()
ob2 = Subtraction()
print(issubclass(Subtraction, Addition))    ## Is Subclass  ?? False
print(issubclass(Calculation, Addition))    ## True
print(isinstance(ob,Calculation))     ## Is Instance ?? True
print(isinstance(ob2,Calculation))    ## False
