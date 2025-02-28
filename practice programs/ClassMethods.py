class Employee :
    company="apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
        @classmethod
        def ChangeCompany(cls,newCompany):
             cls.company=newCompany

e1=Employee()
e1.name="karthik"
e1.show()
e1.ChangeCompany("tesla")
e1.show()
print(Employee.company)