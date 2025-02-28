class student :
    count=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        student.count+=1
        # this is an instance method
    def get_info(self):
        return f"{self.name}{self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total # of students :{cls.count}"
    

student1=student("abc",10)

student2=student("abdc",10)
student3=student("abcd",10)
print(student.get_count())  



