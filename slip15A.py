class Student:
    def Accept(self):
        self.name = input("Enter Student Name: ") 
        self.mark = int(input("Enter Student Total Marks: ")) 
    
    def Modify(self):
        self.oldmark = self.mark
        self.mark = self.mark + int(input("Enter marks to add to student's total: "))
        print("Student Name:", self.name)
        print("Old Total Marks:", self.oldmark)
        print("New Total Marks:", self.mark)
        
# main body
stud1 = Student()
stud1.Accept()
stud1.Modify()
