class RBI:
    def getroi(self):
        return 10

class ICICI(RBI):
    def getroi(self):
        return 5

class SBI(RBI):
    def getroi(self):
        return 7

class HDFC:
    def getroi(self):
        return 9


## creating objects of class##

ob = HDFC()
ob2 = ICICI()
ob3 = SBI()
ob4 = RBI()

#calling methods whose object is invoked
print(ob.getroi())
print(ob2.getroi())
print(ob4.getroi())
print(ob3.getroi())