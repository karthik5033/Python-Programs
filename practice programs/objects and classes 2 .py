class faculty:
    def putdata(self):
        self.id=int(input("enter faculty id :"))
        self.name=input("enter name : ")
        self.salery=float(input("enter faculty salery : "))
    def display(self):
        print("faculty id :",self.id)
        print("faculty name :",self.name)
        print("faculty salery: ",self.salery)
a=faculty()
a.putdata()
a.display()