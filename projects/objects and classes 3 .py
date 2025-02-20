class student:
    def __init__(self,roll,name,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks)


student1=student(12,"karthik",[100,97,90,100])
student2=student(13,"mahesh",[100,97,50,100])
student3=student(14,"suresh",[100,97,90,10])
student4=student(15,"girish",[100,97,94,100])
student5=student(16,"varun",[100,97,90,100])
student6=student(17,"rajesh",[100,97,80,100])

print(student1.average())
    