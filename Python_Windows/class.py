class EMPLOYEE:    ##class is defined

    id = 3456
    name = "Zain"
    def display(self):    ##display function
        print("ID is: %d\n Name is: %s"%(self.id,self.name))

emp = EMPLOYEE()   ##Default constructor
# del emp.id
# del emp
emp.display()      ##method to invoke the function
