class StudentADT:
    def __init__(self):
        self.students = {}

    def addStudent(self, id, name, age, grades):
        self.students[id] = {"Name": name, "Age": age, "Grades": grades}

    def getStudent(self, id):
        return self.students.get(id, None)

    def updateStudent(self, id, newData):
        if id in self.students:
            self.students[id].update(newData)

    def deleteStudent(self, id):
        if id in self.students:
            del self.students[id]

# Using the implementation
students = StudentADT()
students.addStudent(1, "Alice", 20, [85, 90, 95])
print(students.getStudent(1))
