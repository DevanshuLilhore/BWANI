# Class and Object
class Dog:
    def __init__(self,name=None,last=None):
        self.name=name
        self.last=last
    def print_name(self):
        print("FIRST NAME : {} LAST NAME : {} ".format(self.name,self.last))
pila1=Dog("RAJU")
pila2=Dog("Dev","Nath")
pila1.print_name()
pila2.print_name()
